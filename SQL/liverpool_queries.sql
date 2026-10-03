-- Liverpool Football Analytics SQL

SELECT *
FROM liverpool_matches;
-- Total completed matches
SELECT COUNT(*) AS total_matches
FROM liverpool_matches
WHERE Result IN ('W', 'D', 'L');