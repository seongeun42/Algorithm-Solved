SELECT D.ID, count(C.PARENT_ID) CHILD_COUNT
FROM ECOLI_DATA D left join ECOLI_DATA C
ON D.ID = C.PARENT_ID
GROUP BY D.ID
ORDER BY D.ID