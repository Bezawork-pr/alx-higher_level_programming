-- Write a script that lists the number of records 
SELECT score, count(score)
FROM second_table
GROUP BY score
HAVING COUNT(score) > 1
ORDER BY score DESC
