## 회귀모델 성능지표 
---

### MAE(Mean Absoulte Error, 평균 절대 오차)

- 실제 정답 값과 예측 값의 차이를 절대값으로 변환한 뒤 합산하여 평균을 구함 
- 특이값이 많은 경우 주로 사용됨 
- 값이 낮을 수록 좋음 

    $MAE = \frac{\sum|y-\hat{h}|}{n}$

- 장점
  - 직관적
  - 정답 및 예측값과 같은 단위를 가짐 
- 단점
  - 실제 정답보다 낮게 예측했는 지, 높게 예측했는 지 파악하기 힘듦 
  - 스케일에 의존적임
    - ex) 삼성전자의 주가가 1,000,000이고 네이버가 70,000일 때, 두 주가를 예측하는 각각 모델의 MSE가 똑같이 5000이 나왔을 경우, 분명 동일한 에러율이 아님에도 동일하게 보여짐 

<br>

### MSE(Mean Squared Error, 평균 제곱 오차)

- 실제 정답 값과 예측 값의 차이를 제곱한 뒤 평균을 구함
- 값이 낮을 수록 좋음

    $MSE = \frac{\sum_{i=1}^n(y-\hat{y})^2}{n}$

- 장점
  - 직관적
- 단점
  - 제곱하기 때문에 1미만의 에러는 작아지고, 그 이상의 에러는 커짐
    - 즉, 값의 왜곡이 있음
  - 실제 정답보다 낮게 예측했는 지, 높게 했는 지 파악하기 힘듦
  - 스케일 의존적임(Scale dependency)

<br>

### RMSE(Root Mean Squared Error, 평귱 제곱근 오차)

- MSE 갓에 루트를 씌워서 에러를 제고해서 생기는 값의 왜곡을 줄이기 위해

    $MSE = \sqrt{\frac{\sum_{i=1}^n(y-\hat{y})^2}{n}}$

- 장점
  - 직관적
- 단점
  - 제곱하기 때문에 1미만의 에러는 작아지고, 그 이상의 에러는 커짐
  - 실제 정답보다 낮게 예측했는 지, 높게 했는 지 파악하기 힘듦
  - 스케일 의존적임(Scale dependency)

<br>

### MAPE(Mean absolute percentage error, 평균 절대 비율 오차)

- MAE를 비율, 퍼센트로 표현하여 스케일 의존적 에러의 문제점을 개선함 
  
  $MAPE = \frac{100}{n}\sum_{i=1}^n|\frac{y-\hat{y}}{y}|$ 

- 장점
  - 직관적
  - 다른 모델과 에러율 비교가 쉬움
- 단점
  - 실제 정답보다 낮게 예측했는 지, 높게 예측했는 지 파악하기 힘듦
  - 실제 정답이 1보다 작을 경우, 무한대의 값으로 수렴할 수 있음 

<br>

### MPE(Mean Percentage Error)

- MAPE에서 절대값을 제외하여 계산 
- 모델이 underperformance인지 overperformance인지 판단 가능(음수이면 overperformance, 양수이면 underperformance)

    $MPE = \frac{100}{n}\sum_{i=1}^n\frac{y-\hat{y}}{y}$

<br>

### R2 score = R square

- 다른 지표(MAE, MSE, RMSE)들은 모델마다 값이 다르기 때문에 절대 값만 보고 성능을 판단하기 어려움
- R2 score는 비교가 쉬움
- 실제 값의 분산 대비 예측값의 분산 비율을 의미함
- 0과 1사이의 값을 가지며 1에 가까울 수록 선형회귀 모델이 데이터에 대해 높은 연관성을 가지고 있다고 해석할 수 있음
  
  $R^2 = 1 - \frac{SSE}{SST} = 1 - \frac{\frac{1}{n}\sum_{i=1}^n(y^{i}-\hat{y}^{i})^2}{\frac{1}{n}\sum_{i=1}^n(y^{i}-m_y)^2} = 1 - \frac{MSE}{var(y)}$

  - SST: 전체 제곱의 합
  - SSE: 제곱 오차항 

    ```python
    from sklearn.metrics import r2_score
    r2 = r2_score(y, lr.predict(x_2))
    # lr = linear regression model
    # lr.predict = 모델의 예측값
    ```

<br>

### Adjusted R Square

- 다변량 회귀분석에서는 독립변수가 유의하든, 유의하지 않든 독립변수의 수가 많아지면 결정계수(R square)가 높아짐 
- 이러한 결정계수의 단점을 보완하기 위해 수정된 결정계수가 필요 
- p=독립변수의 갯수를 뜻하는 데, p가 분모에 위치하면서 p가 증가함에 따라 분자에 있는 R square 값도 증가하는 영향을 어느정도 상쇄해줌 
- 따라서 독립변수의 갯수를 고려하기 때문에 수정된 결정계수가 결정계수를 보완해줄 수 있음 
- 보통 수정된 결정계수는 결정계수보다 작은 값으로 산출되는 특징이 있음

    $R_a^2 = 1 - \frac{(n-1)(1-R^2)}{n - p - 1} = 1 - \frac{(n-1)(\frac{SSE}{SST})}{n - p - 1} = 1 - (n-1)\frac{MSE}{SST}$

---

#### 참고자료

@ https://white-joy.tistory.com/10

@ https://dailyheumsi.tistory.com/167

@ https://go-hard.tistory.com/125
