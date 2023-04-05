-- 코드를 입력하세요
SELECT ORDER_ID, PRODUCT_ID, date_format(OUT_DATE, "%Y-%m-%d") OUT_DATE,
    (case when OUT_DATE < "2022-05-02" then "출고완료"
     when OUT_DATE IS NULL then "출고미정"
    else "출고대기" end) 출고여부
FROM FOOD_ORDER
ORDER BY ORDER_ID