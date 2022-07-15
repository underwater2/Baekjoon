-- 1. SELECT문에서 Alias를 붙일 때는 '' 없이 소문자로 (대문자도 가능하지만 구분하기 쉽게 소문자로.)
-- 2. Alias는 다른 절에서도 변수처럼 사용할 수 있다.
-- 3. SQL에서는 기본적으로 GROUP BY 절에 있거나 집계 함수가 사용된 컬럼만을 HAVING 절에서 사용할 수 있고, MySQL에서는 SELECT 문에 사용된 컬럼을 사용하는 것도 허용된다. 그런데 HOUR(DATETIME)는 컬럼 이름 앞에 함수가 붙었고, 그 함수가 집계 함수가 아니라 산술 함수이므로, HAVING절에서는 사용할 수 없는 것이다.
    -- 출처: https://velog.io/@ready2start/MySQL-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%9E%85%EC%96%91-%EC%8B%9C%EA%B0%81-%EA%B5%AC%ED%95%98%EA%B8%B0-1
    
# SELECT HOUR(DATETIME) AS hour, COUNT(*) AS count
# FROM ANIMAL_OUTS 
# GROUP BY hour
# HAVING hour BETWEEN 9 AND 19
# ORDER BY hour ASC
# ;

SELECT HOUR(DATETIME) AS 'HOUR', COUNT(HOUR(DATETIME)) AS 'COUNT' 
FROM ANIMAL_OUTS 
WHERE HOUR(DATETIME) >= 9 AND HOUR(DATETIME) <= 19 
GROUP BY HOUR(DATETIME) 
ORDER BY HOUR(DATETIME)