-- 코드를 입력하세요
SELECT COUNT(*) as USERS
FROM USER_INFO
WHERE AGE >= 20 AND AGE <= 29 AND JOINED <= '2021-12-31'