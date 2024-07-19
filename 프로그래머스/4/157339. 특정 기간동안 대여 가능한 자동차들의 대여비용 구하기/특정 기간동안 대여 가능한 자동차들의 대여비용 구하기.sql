SELECT *
FROM (SELECT CAR_ID, S.CAR_TYPE,
       round(DAILY_FEE * ((100 - convert(replace(DISCOUNT_RATE, '%', ''), unsigned)) / 100) * 30) FEE
FROM (SELECT  CAR_ID, CAR_TYPE, DAILY_FEE
      FROM    CAR_RENTAL_COMPANY_CAR
      WHERE   CAR_TYPE in ('SUV', '세단')
      and     CAR_ID not in (SELECT distinct CAR_ID
                         FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                         WHERE END_DATE >= "2022-11-01"
                         or START_DATE between "2022-11-01" and "2022-11-30")) S
      LEFT JOIN  CAR_RENTAL_COMPANY_DISCOUNT_PLAN P
      ON S.CAR_TYPE = P.CAR_TYPE and P.DURATION_TYPE like "%30%") T
WHERE FEE >= 500000 and FEE < 2000000
ORDER BY FEE desc, CAR_TYPE, CAR_ID desc