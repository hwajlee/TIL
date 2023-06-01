## 특정 테이블의 데이터 삭제 명령어 
---

|DROP               |TRUNCATE             |DELETE               |
|-------------------|---------------------|---------------------|
|DDL                |DDL(일부 DML 성격 가짐)| DML                |
|ROLLBACK 불가능    |ROLLBACK 불가능       |COMMIT 이전 ROLLBACK 가능 |
|Auto Commit       |Auto Commit           |사용자 Commit         |
|테이블이 사용했던 Storage를 모두 Release|테이블이 사용했던 Storage중 최초 테이블 생성 시 할당된 storage만 남기고 Release|데이터를 모두 Delete해도 사용했던 Storage는 Release되지 않음|
|테이블의 정의 자체를 완전히 삭제|테이블을 최초 생성된 초기상태로 만듦|데이터만 삭제|

- 특정 테이블의 모든 데이터를 삭제하고, 디스크 용량을 초기화하여 로그를 남기지 않기 위해서는 TRUNCATE TABLE 명령을 사용해야 한다. 
- DELECTE TABLE은 테이블의 데이터를 모두 삭제하지만, 디스크 사용량을 초기화하지는 않아 로그가 남는다. 
- DROP TABLE은 테이블의 데이터를 모두 삭제하고 디스크 사용량도 없앨(초기화) 수 있지만 , 테이블의 스키마 정의도 함께 삭제된다.