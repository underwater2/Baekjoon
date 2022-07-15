-- 쿼리문에서 로컬 변수를 활용하는 문제
-- 풀이 참고: https://chanhuiseok.github.io/posts/db-6/

SET @hour := -1;  -- 변수 선언

SELECT (@hour := @hour + 1) AS hour,
    (SELECT COUNT(*) 
     FROM ANIMAL_OUTS 
     WHERE HOUR(DATETIME) = @hour) AS count
FROM ANIMAL_OUTS
WHERE @hour < 23
;