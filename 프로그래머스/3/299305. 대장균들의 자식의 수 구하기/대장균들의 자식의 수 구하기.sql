SELECT ID, ifnull(CHILD_COUNT, 0) CHILD_COUNT
FROM ECOLI_DATA D left join (SELECT PARENT_ID, count(PARENT_ID) CHILD_COUNT
                             FROM ECOLI_DATA
                             GROUP BY PARENT_ID
                             HAVING PARENT_ID is not null) C
ON D.ID = C.PARENT_ID
ORDER BY ID