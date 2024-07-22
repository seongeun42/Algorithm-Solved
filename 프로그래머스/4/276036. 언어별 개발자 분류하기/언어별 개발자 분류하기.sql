SELECT CASE
    WHEN sum(NAME = "Python") > 0 and sum(CATEGORY = "Front End") > 0 THEN "A"
    WHEN sum(NAME = "C#") > 0 THEN "B"
    WHEN sum(CATEGORY = "Front End") > 0 THEN "C"
    END GRADE,
    ID, EMAIL
FROM DEVELOPERS D join SKILLCODES S
ON D.SKILL_CODE & S.CODE != 0
GROUP BY ID, EMAIL
HAVING sum(NAME = "Python") > 0 and sum(CATEGORY = "Front End") > 0
    or sum(NAME = "C#") > 0
    or sum(NAME = "Python") = 0 and sum(CATEGORY = "Front End") > 0
ORDER BY GRADE, ID