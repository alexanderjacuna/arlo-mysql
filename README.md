# arlo-mysql
Python script developed by Michael Stewart and Alexander Acuna that sends Alro readings to Mysql.

SELECT
  UNIX_TIMESTAMP(timestamp) AS "time",
  battery_level as value,
  name as metric
FROM arlo.telemetry
WHERE
  $__timeFilter(timestamp)
ORDER BY UNIX_TIMESTAMP(timestamp)
