-- 코드를 입력하세요
SELECT UGB.TITLE,
       UGB.BOARD_ID,
       UGR.REPLY_ID, 
       UGR.WRITER_ID, 
       UGR.CONTENTS, 
       DATE_FORMAT(UGR.CREATED_DATE, '%Y-%m-%d') as DATE_FORMAT
FROM USED_GOODS_BOARD UGB
    JOIN USED_GOODS_REPLY UGR ON UGB.BOARD_ID = UGR.BOARD_ID
WHERE DATE_FORMAT(UGB.CREATED_DATE, '%Y-%m') = '2022-10'
ORDER BY 6, 1