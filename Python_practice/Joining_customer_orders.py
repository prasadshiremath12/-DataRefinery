import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


def parse_order(line):
    """Parses order CSV line, casts data types, and computes calculated fields."""
    parts = line.strip().split(",")
    amount = float(parts[2])  # Type cast: str -> float

    return {
        "order_id": parts[0],
        "customer_id": parts[1],
        "amount": amount,
        "tax": round(amount * 0.10, 2)  # Row transformation: calculated tax field
    }


def parse_customer(line):
    """Parses customer CSV line into (key, value) tuple for AsDict."""
    parts = line.strip().split(",")
    customer_id = parts[0]

    return (customer_id, {
        "name": parts[1].strip().title(),  # Row transformation: proper name casing
        "city": parts[2].strip().upper()  # Row transformation: uppercase city
    })


def format_output(order, customers_side_input):
    """Enriches order dictionary with customer details from side input."""
    customer_id = order["customer_id"]
    customer_details = customers_side_input.get(
        customer_id,
        {"name": "UNKNOWN", "city": "UNKNOWN"}
    )

    return {
        **order,
        "name": customer_details["name"],
        "city": customer_details["city"]
    }


def aggregate_city_sales(city_orders):
    """Aggregates total sales, total tax, and order counts per city."""
    city, orders = city_orders
    total_sales = sum(o["amount"] for o in orders)
    total_tax = sum(o["tax"] for o in orders)
    total_orders = len(orders)

    return {
        "city": city,
        "total_orders": total_orders,
        "total_sales": round(total_sales, 2),
        "total_tax": round(total_tax, 2)
    }


def run():
    options = PipelineOptions(
        runner='DirectRunner',
        project='gcp-project',
        region='us-central1',
        temp_location='gs://gcp-bucket/temp',
        staging_location='gs://gcp-bucket/staging'
    )

    with beam.Pipeline(options=options) as pipeline:
        # 1. Read & Row Transform Orders
        orders_pipeline = (
                pipeline
                | "Read Orders" >> beam.io.ReadFromText(r"D:\orders.csv", skip_header_lines=1)
                | "Parse & Transform Orders" >> beam.Map(parse_order)
        )

        # 2. Read & Row Transform Customers
        customers_pipeline = (
                pipeline
                | "Read Customers" >> beam.io.ReadFromText(r"D:\Customers.csv", skip_header_lines=1)
                | "Parse & Transform Customers" >> beam.Map(parse_customer)
        )

        customer_dict = beam.pvalue.AsDict(customers_pipeline)

        # 3. Join Tables
        joined_orders = (
                orders_pipeline
                | "Join Customer Details" >> beam.Map(format_output, customers_side_input=customer_dict)
        )

        # 4. Aggregation: Group joined orders by City and sum sales/tax
        city_aggregations = (
                joined_orders
                | "Map to (City, Order) KV" >> beam.Map(lambda order: (order["city"], order))
                | "Group by City" >> beam.GroupByKey()
                | "Aggregate Metrics" >> beam.Map(aggregate_city_sales)
        )

        # 5. Output Results
        joined_orders | "Print Enriched Orders" >> beam.Map(lambda x: print(f"ORDER: {x}"))
        city_aggregations | "Print Aggregated City Metrics" >> beam.Map(lambda x: print(f"AGGREGATION: {x}"))


if __name__ == "__main__":
    run()