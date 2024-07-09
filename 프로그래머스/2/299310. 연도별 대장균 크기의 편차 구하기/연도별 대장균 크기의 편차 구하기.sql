SELECT year(DIFFERENTIATION_DATE) YEAR, max(SIZE_OF_COLONY) over (partition by year(DIFFERENTIATION_DATE)) - SIZE_OF_COLONY YEAR_DEV, ID
FROM ECOLI_DATA
ORDER BY YEAR, YEAR_DEV