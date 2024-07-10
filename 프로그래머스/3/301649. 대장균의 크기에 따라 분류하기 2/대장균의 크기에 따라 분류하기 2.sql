SELECT ID, CASE
            WHEN PERCENT > 75 THEN "LOW"
            WHEN PERCENT > 50 THEN "MEDIUM"
            WHEN PERCENT > 25 THEN "HIGH"
            ELSE "CRITICAL"
           END COLONY_NAME
FROM ECOLI_DATA E natural join (SELECT ID, percent_rank() over (order by SIZE_OF_COLONY desc) * 100 PERCENT
                                FROM ECOLI_DATA) P
ORDER BY ID