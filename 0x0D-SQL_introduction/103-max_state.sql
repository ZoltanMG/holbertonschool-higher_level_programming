-- Convert database of UTF8
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC
LIMIT 3;
