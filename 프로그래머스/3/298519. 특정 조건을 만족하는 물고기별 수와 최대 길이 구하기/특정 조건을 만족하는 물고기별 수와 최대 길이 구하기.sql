SELECT count(*) FISH_COUNT , max(LENGTH) MAX_LENGTH, FISH_TYPE
FROM FISH_INFO
GROUP BY FISH_TYPE
HAVING avg(ifnull(LENGTH, 10)) >= 33
ORDER BY FISH_TYPE