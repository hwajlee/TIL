## 연산자 LIKE 
---
- 문자열의 패턴을 검색하는 데 사용 
- 특정 키워드만 포함된 컬럼을 추출 가능 

<br>

### 기본적인 사용법 
```SQL
SELECT * FROM 테이블 WHERE 칼럼 LIKE 'PATTERN'
```
- 패턴 종류 
  - %: 모든 문자
  - _: 한 글자 

<br>

### 예시 
- 라면 테이블 
  
|id         |NAME        |PRICE      |
|-----------|------------|-----------|
|1          |짜장라면     |1000       |
|2          |스파게티     |1000       |
|3          |라면         |800        |
|4          |진라면 큰컵  |1200       |
|5          |라면볶이     |1500       |

1. '라면' 키워드를 포함하고 있는 행을 모두 출력하고 싶다면? (NAME 칼럼에 데이터 중 앞 뒤에 무슨 글자가 오던지 '라면'을 포함하고 있다면 출력)
   ```SQL
   SELECT * FROM TABLE WHERE NAME LIKE '%라면%'
   ```

   - 결과: 1, 3, 4, 5행 출력 ('라면' 글자가 없는 2행을 제외하고 모두 출력됨)

<br>

2. '라면'으로 끝나는 문자가 있는 행 출력 
   ```SQL
   SELECT * FROM TABLE WHERE NAME LIKE '%라면'
   ```
   
   - 결과: 1, 3행 출력 

<br>

3. '라면'으로 시작하는 문자가 있는 행 출력 
   ```SQL
   SELECT * FROM TABLE WHERE LIKE '라면%'
   ```

   - 결과: 3, 5행 출력 

<br>

4. 한 글자 뒤에 '라면' 글자가 있는 행 출력
   ```SQL
   SELECT * FROM TABLE WHERE LIKE '_라면%'
   ```

   - 결과: 4행 출력 

<br>

5. '라면' 문자 앞 뒤로 2개의 문자가 있는 행 출력 
   ```SQL
   SELECT * FROM TABLE WHERE NAME LIKE '__라면__'
   ```

   - 결과: 아무것도 출력 X 

<br>

6. 컬럼 데이터가 '라면'인 행 출력 
   ```SQL
   SELECT * FROM TABLE WHERE NAME LIKE '라면'
   ```

   - 결과: 3행 출력 

<br>

---
#### 참고자료
https://lcs1245.tistory.com/entry/SQL-LIKE-%EC%97%B0%EC%82%B0%EC%9E%90-%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%B6%80%EB%B6%84%EC%9D%BC%EC%B9%98-%EA%B2%80%EC%83%89