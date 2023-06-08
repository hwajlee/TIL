## Join 절의 ON과 WHERE절 차이 
---
- JOIN 하는 범위가 다름 
- 예시) 

```sql
-- 1) 
SELECT *
FROM test1 a LEFT JOIN test2 b
ON (a.bb = b.aa)
WHERE b.cc = 7;

-- 2)
SELECT *
FROM test1 a LEFT JOIN test2 b
ON (a.bb = b.aa AND b.cc = 7);
```

- 1)의 경우는 a와 b 테이블의 OUTER JOIN을 수행한 후에 b.cc = 7인 테이블을 추출
- 2)의 경우는 (a테이블)과 (b테이블 중 b.cc = 7인 경우)를 OUTER JOIN한 결과가 나옴 
  - 따라서 1)의 결과는 b.cc = 7인 데이터만 존재하지만 2)의 결과는 b.cc = 7이 아닌 데이터 존재 

<br>

- test1 테이블
  
|aa  |bb  |
|----|----|
|1   |4   |
|2   |5   |
|3   |6   |

- test2 테이블 
  
|aa  |cc  |
|----|----|
|1   |7   |
|2   |8   |

<br>

- 1)번 결과 

|aa  |bb  |aa  |cc  |
|----|----|----|----|
|1   |4   |1   |7   |

- 2)번 결과 

|aa  |bb  |aa  |cc  |
|----|----|----|----|
|1   |4   |1   |7   |
|2   |5   |NULL|NULL|
|3   |6   |NULL|NULL|


<br>

#### 추가) 실행순서 
- FROM: 조회 테이블 확인 
- ON: 조인 조건 확인 
- JOIN: 테이블 조인(병합)
- WHERE: 데이터 추출 조건 확인 
- GROUP BY: 특정 컬럼 그룹화 
- HAVING: 그룹화 이후 데이터 추출
- SELECT: 데이터 추출
- DISTINCT: 중복 제거
- ORDER BY: 데이터 순서 정렬 

<br>

---
#### 참고자료 
@ https://blog.leocat.kr/notes/2017/07/28/sql-join-on-vs-where

@ https://soo-vely-dev.tistory.com/220