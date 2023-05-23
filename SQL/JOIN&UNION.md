## JOIN
---
- 두 개의 테이블을 서로 묶어서 데이터를 검색하는 방법
- 연결하기 위해서는 테이블이 **적어도 하나의 컬럼을 공유**해야 함 
  
  ![](./img/joins.png)

  출처: &nbsp;https://lyk00331.tistory.com/107

<br>

### INNER JOIN(내부 조인)
- 두 테이블을 조인할 때, 두 테이블에 모두 지정한 열의 테이터가 존재해야 함
- **교집합**
  ![](./img/inner_join.png)

```MySQL
SELECT <열 목록>
FROM <첫 번째 테이블>
    JOIN <두 번째 테이블>
    ON <조인될 조건>
[WHERE 검색 조건]
```

- INNER JOIN을 JOIN이라고만 써도 INNER JOIN으로 인식함 
  
  
```MySQL
SELECT <열 목록>
FROM <첫 번째 테이블>, <두 번째 테이블>

WHERE 조인될 조건 AND 검색 조건 
```

- "," = JOIN 
- ON에 쓸 조인 조건을 WHERE에 써서 더욱 간략하게 작성 가능 

<br>

### OUTER JOIN(외부 조인)
- 두 테이블을 조인할 때, **1개의 테이블에만 데이터가 있어도** 결과가 나옴
- **합집합**
  ![](./img/outer_join.png)

```MySQL
SELECT <열 목록>
FROM <첫 번째 테이블(LEFT 테이블)>
        <LEFT | RIGHT | FULL> OUTER JOIN <두 번째 테이블(RIGHT 테이블)>
        ON <조인될 조건>
[WHERE 검색 조건]
```
- LEFT OUTER JOIN - 왼쪽 테이블 모든 값 출력 
- RIGHT OUTER JOIN - 오른쪽 테이블 모든 값 출력 
- FULL JOIN - 왼쪽, 오른쪽 테이블 모든 값 출력 

<br>

### CROSS JOIN(상호 조인)
- 한쪽 테이블의 모든 행과 다른 쪽 테이블의 모든 행을 조인
- 상호 조인의 결과, 전체 행 개수는 두 테이블의 각 행수를 곱한 수 
- 카디션 곱(CARTESIAN PRODUCT)라고도 함 
  ![](./img/cross_join.png)

```MySQL
SELECT *
FROM <첫 번째 테이블>
    CROSS JOIN <두 번째 테이블>
```

<br>

### SELF JOIN(셀프 조인)
- 자신과 자신이 조인한다는 의미 
- 1개의 테이블 사용 
  ![](./IMG/self_join.png)

```MySQL
SELECT <열 목록>
FROM <테이블> 별칭 A
    INNER JOIN <테이블> 별칭 B
    ON <조인될 조건>
[WHERE 검색 조건]
```

<br>

## UNION
---
- 여러 개의 SELECT문의 결과를 단일 세트로 연결 표현할 때 사용 
- 합친 결과에서 중복되는 행은 하나만 표시 
  - DISTINCT 키워드를 따로 명시하지 않아도 기본적으로 중복되는 레코드를 제거 
- UNION 내의 각 SELECT문을 **같은 수의 열**을 가져야 함 
- 각각 SELECT문의 열을 또한 **동일한 순서**로 있어야 함 
- 열은 **호환되는 데이터 형식**을 가져야 함 
  ![](./IMG/UNION.png)
  
  출처: https://www.devart.com/dbforge/sql/sqlcomplete/union-vs-union-all.html

```MySQL
SELECT * FROM A
UNION (ALL)
SELECT * FROM B
```

<br>

### uUNION ALL 
-두 SQL문의 결과를 결합하는 데 사용 
- UNION과 UNION ALL의 차이  
  - UNION ALL의 경우 데이터 값이 중복하더라도 조건에 일치하는 데이터를 모두 표시 
  - 즉, 중복 제거하지 않음
  
  ![](./img/UNIONALL.png)

<br>

## JOIN vs UNION
---
![](./IMG/UNION&JOIN.png)

출처: https://lyk00331.tistory.com/m/110
