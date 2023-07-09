테이블명: ANIMAL_INS
- 컬럼
  - ANIMAL_ID
  - ANIMAL_TYPE
  - DATETIME
  - INTAKE_CONDITION
  - NAME
  - SEX_UPON_INTAKE

<br>

문제
- 입양 게시판에 동물 정보를 게시하려 합니다. 동물의 생물 종, 이름, 성별 및 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요. 이때 프로그래밍을 모르는 사람들은 NULL이라는 기호를 모르기 때문에, 이름이 없는 동물의 이름은 "No name"으로 표시해 주세요.

<br>

풀이
- IFNULL(컬럼명, null일 경우 대체값)을 사용해서 NAME 컬럼에서 NULL값인 경우 No name이라고 대체되어 표시되도록 할 것 

<br>

- 
```sql
SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name') as NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
```