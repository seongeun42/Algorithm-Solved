SELECT A.AUTHOR_ID, AUTHOR_NAME, CATEGORY, sum(PRICE * SALES) TOTAL_SALES
FROM BOOK_SALES S
    left join BOOK B on S.BOOK_ID = B.BOOK_ID and date_format(SALES_DATE, '%y%m') = '2201'
    join AUTHOR A on B.AUTHOR_ID = A.AUTHOR_ID
GROUP BY AUTHOR_ID, CATEGORY
ORDER BY AUTHOR_ID, CATEGORY desc





# FROM AUTHOR A natural join (SELECT AUTHOR_ID, CATEGORY, PRICE * sum(SALES) TOTAL_SALES
#                     FROM BOOK B natural join BOOK_SALES S
#                     WHERE date_format(SALES_DATE, '%y%m') = '2201'
#                     GROUP BY AUTHOR_ID, CATEGORY) S