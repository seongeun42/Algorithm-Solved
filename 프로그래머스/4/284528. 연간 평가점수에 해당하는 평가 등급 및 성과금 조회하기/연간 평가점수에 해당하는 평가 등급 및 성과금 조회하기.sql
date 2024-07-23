SELECT EMP_NO, EMP_NAME, GRADE,
        case
            when GRADE = "S" then SAL * 0.2
            when GRADE = "A" then SAL * 0.15
            when GRADE = "B" then SAL * 0.1
            else 0
        end BONUS
FROM HR_EMPLOYEES E natural join (SELECT EMP_NO,
                                    case
                                        when avg(SCORE) >= 96 then "S"
                                        when avg(SCORE) >= 90 then "A"
                                        when avg(SCORE) >= 80 then "B"
                                        else "C"
                                    end GRADE
                                  FROM HR_GRADE
                                  GROUP BY EMP_NO) G
ORDER BY EMP_NO