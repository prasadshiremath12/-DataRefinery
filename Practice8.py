
#Count the records after INNER, LEFT, RIGHT JOIN
TABLE 1: column a , values = 1,1,1,2,3,3, Null
    TABLE 2: column b , values = 1,1,4,4, Null



# OPtimize the following query by replacing the subquery with a JOIN:
SELECT
  t.user_id,
  t.transaction_id,
  t.amount,
  (SELECT status FROM `my-gcp-migration-project.landing_zone.user_profiles` u
   WHERE u.user_id = t.user_id AND u.updated_at <= t.event_timestamp
   ORDER BY u.updated_at DESC LIMIT 1) AS historical_status
FROM `my-gcp-migration-project.landing_zone.streaming_events_cdc` t
WHERE t._PARTITIONDATE = '2026-06-01';

# After JOIN optimizaton
WITH latest_status AS (
  SELECT
    u.user_id,
    u.status,
    u.updated_at,
    ROW_NUMBER() OVER (
      PARTITION BY u.user_id
      ORDER BY u.updated_at DESC
    ) AS rn
  FROM `my-gcp-migration-project.landing_zone.user_profiles` u
)

SELECT
  t.user_id,
  t.transaction_id,
  t.amount,
  ls.status AS historical_status
FROM `my-gcp-migration-project.landing_zone.streaming_events_cdc` t
LEFT JOIN latest_status ls
  ON t.user_id = ls.user_id
 AND ls.updated_at <= t.event_timestamp
WHERE t._PARTITIONDATE = '2026-06-01'
AND ls.rn = 1;
