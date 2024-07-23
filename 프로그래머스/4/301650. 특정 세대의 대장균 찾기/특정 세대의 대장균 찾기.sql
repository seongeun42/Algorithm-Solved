SELECT ID
FROM ECOLI_DATA
WHERE PARENT_ID in (SELECT ID
                    FROM ECOLI_DATA
                    WHERE PARENT_ID in (SELECT ID
                                        FROM ECOLI_DATA
                                        WHERE PARENT_ID is null))
ORDER BY ID