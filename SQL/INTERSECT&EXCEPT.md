## 교집합(INTERSECT)와 차집합(EXCEPT)
---

### 교집합 
- SELECT * FROM TableA INTERSECT SELECT * FROM TableB 
- 교집합 개념 (Inner Join 생각하기)
- 중복된 행은 하나의 행으로 만듦 (Union 특징과 똑같음)

<br>

### 차집합
- SELECT * FROM TableA EXCEPT SELECT * FROM TableB
- TableA Row 내용 중 TableB와 Row 내용이 같지 않거나 TableA에 있는데 TableB에는 없는 데이터를 리턴 
- 차집합 개념 
- NOT IN 또는 NOT EXISTS로 대체 가능 
- 중복된 행은 하나의 행으로 만듦

<br>

### 주의 사항
- TableA와 TableB 컬럼의 갯수와 순서가 동일해야함
- 각 상호 비교되는 컬럼들의 데이터 형식이 호환되어야 함

---
#### 참고자료 
@ https://rocabilly.tistory.com/50