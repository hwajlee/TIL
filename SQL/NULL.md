## NULL
---

### COUNT 

```MySQL
INSERT INTO TEST37 VALUES(NULL, 10);
INSERT INTO TEST37 VALUES(12, NULL);
INSERT INTO TEST37 VALUES(12, NULL);
INSERT INTO TEST37 VALUES(NULL, NULL);
INSERT INTO TEST37 VALUES(10, 12);
``` 

- 전체 행의 갯수 COUNT 

    ```SQL
    SELECT COUNT(*) FROM TEST37;
    ```

    - 전체 행의 갯수를 반환할 때는 `NULL 포함`
    - 따라서 반환되는 행 갯수 4개 
  
        |COUNT(*)|
        |--------|
        |4       |


- 특정 컬럼만 COUNT 
  
    ```SQL
    SELECT COUNT(COL1) FROM TEST37;
    ```

    - 컬럼명을 지정할 경우 `NULL 미포함` 
    - 반한되는 행 갯수 2개 

  
        |COUNT(COL1)|
        |-----------|
        |2          |

<br>

### IN

- IN()에 NULL 포함 
  
  ```SQL
  SELECT * FROM TEST37 WHERE COL1 IN(12, 10, NULL);
  ```

  - IN은 AND가 아니라 OR이며, `NULL은 제외`하고 값을 출력됨
  - 반환되는 행 갯수 2개
  
    |COL1|COL2|
    |----|----|
    |12  |    |
    |10  |12  |

<br>

### GROUP BY

- NULL이 포함된 컬럼을 기준으로 GROUP BY한 경우 

    ```SQL
    SELECT COL1, COUNT(*) FROM TEST37 GROUP BY(COL1);
    ```

    - NULL 또한 하나의 그룹으로 묶여 총 3행이 반환됨 

    |COL1|COUNT(*)|
    |----|--------|
    |    |2       |
    |12  |1       |
    |10  |1       |


