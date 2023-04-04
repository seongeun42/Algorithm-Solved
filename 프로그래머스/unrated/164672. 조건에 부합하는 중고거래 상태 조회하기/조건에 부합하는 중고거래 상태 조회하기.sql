-- 코드를 입력하세요
SELECT BOARD_ID, WRITER_ID, TITLE, PRICE, 
    (case 
     when STATUS = "SALE" then "판매중"
     when STATUS = "RESERVED" then "예약중"
     else "거래완료"
     end) STATUS
FROM USED_GOODS_BOARD
WHERE CREATED_DATE = "2022-10-05"
ORDER BY 1 desc