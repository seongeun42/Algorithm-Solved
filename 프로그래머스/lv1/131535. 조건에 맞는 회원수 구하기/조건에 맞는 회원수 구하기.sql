-- 코드를 입력하세요
SELECT count(*) as USERS
FROM USER_INFO
WHERE year(JOINED) = '2021'
AND AGE >= 20 and AGE <= 29;