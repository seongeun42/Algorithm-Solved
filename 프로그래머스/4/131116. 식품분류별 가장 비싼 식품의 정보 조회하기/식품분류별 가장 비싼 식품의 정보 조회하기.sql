SELECT CATEGORY, PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE (CATEGORY, PRICE) in (SELECT CATEGORY, max(PRICE)
                   FROM FOOD_PRODUCT
                   WHERE CATEGORY in ('과자', '국', '김치', '식용유')
                   GROUP BY CATEGORY)
ORDER BY PRICE desc