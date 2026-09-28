employees = {
    101: {'Name': 'Satya', 'Age': 27, 'Department': 'HR', 'Salary': 50000.0},
    102: {'Name': 'Prasad', 'Age': 30, 'Department': 'Engineering', 'Salary': 75000.0},
    103: {'Name': 'Ananya', 'Age': 25, 'Department': 'Marketing', 'Salary': 60000.0}
}

def add_employee():
    """Step 3: Function to add a new employee with unique ID validation."""
    print("\n--- Add New Employee ---")

    # Input and validate unique Employee ID
    # 1. Enter validation loop for Employee ID
    while True:
        try:
            Employee_id = int(input("Enter employee ID: "))
            if Employee_id in employees:
                print(f"Employee with Employee_id {Employee_id} already exists")
                break  # <--- ONLY breaks out of this ID validation loop!
            # 2. Enter validation loop for Age

            Age = input("Enter Employee Age: ")
            if Age < 0:
                print(f"Invalid Age {Age} \nPlease enter a valid positive integer")
                break  # <--- ONLY breaks out of the Age validation loop!

            # 3. Execution continues down to the Name prompt
            Name= input("Enter Employee Name: ").strip()
            # ... collects Department and Salary ...
            Department = input("Enter Employee Department: ")
            Salary = input("Enter Employee Salary: ")

            # 4. Stores the employee in the dictionary
            employees[Employee_id] = {'Name': Name, 'Age': Age, 'Department': Department, 'Salary': Salary}
            print(f"Employee with {Name} and Employee Id {Employee_id} has been added successfully")
            return employees

        except:
            print("Invalid input! Please enter a valid input.")
    # 5. Function finishes and returns back to main_menu()

def view_employees():
    """Step 4: Function to view all employees in a formatted table."""
    print("\n--- All Employee Records ---")

    if not employees:
        print("No employees available.")
        return

    # Print Table Header
    header = f"{'ID':<8} | {'Name':<15} | {'Age':<5} | {'Department':<15} | {'Salary (Rs.)':<12}"
    divider = "-" * len(header)

    print(divider)
    print(header)
    print(divider)

    # Print Each Employee Row
    for emp_id, details in employees.items():
        print(
            f"{emp_id:<8} | "
            f"{details['Name']:<15} | "
            f"{details['Age']:<5} | "
            f"{details['Department']:<15} | "
            f"{details['Salary']:<12.2f}"
        )
    print(divider)

def search_employee():
    try:
        employee_id = int(input("Enter employee ID to search: "))
    except ValueError:
        print("Invalid input! Please enter a valid input.")
        return

    if employee_id in employees:
        emp=employees[employee_id]
        print("\nEmployee found")
        print(f"ID:{employee_id}")
        print(f"Name:{emp['Name']}")
        print(f"Age:{emp['Age']}")
        print(f"Department:{emp['Department']}")
        print(f"Salary:{emp['Salary']}")
    else:
        print("\n Employee not found")


# Step 2 - Define the Menu System
# Create a menu that displays the following options
def Menu():
    while True:
        print("\n==============================")
        print("EMPLOYEE MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add New Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Exit")
        print("================================")

        choice=input("Enter your choice: ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice==4:
            print("Thank you for using Employee Management System, Good bye!")
            break
        else:
            print("Invalid input! Please enter a valid input. from 1 to 4")

if __name__=="__main__":
    Menu()