-- Write a script that lists the number of records
-- change count(score) to num for colomn name
SELECT score, count(score) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC
