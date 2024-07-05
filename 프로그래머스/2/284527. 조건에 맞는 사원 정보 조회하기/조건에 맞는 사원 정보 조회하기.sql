SELECT S.T_SCORE SCORE, E.EMP_NO, EMP_NAME, POSITION, EMAIL
FROM HR_EMPLOYEES E JOIN (SELECT EMP_NO, sum(SCORE) T_SCORE
                        FROM HR_GRADE
                        WHERE YEAR = 2022
                        GROUP BY EMP_NO
                        ORDER BY T_SCORE desc
                        LIMIT 1) S
ON E.EMP_NO = S.EMP_NO