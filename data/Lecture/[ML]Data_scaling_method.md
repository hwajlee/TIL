## Data scaling method 
---
- 앞서 Numerical data preprocessing 방법에서 데이터 스케일링 종류에 Standard scaler, Min-Max scaler, Robust scaler가 있음을 확인함 
- 스케일링 할 때 사용하는 메서드
    - fit_transform()
        - fit()과 transform()을 한 번에 처리할 수 있게 하는 메서드인데, **test data에는 fit_transform() 메서드를 쓰면 안됨**
        - fit(): 데이터를 학습시키는 메서드 
    - transform(): 실제로 학습시킨 것을 적용하는 메서드 

<br>

### code 

```python
# 1. 라이브러리 호출
from sklearn.preprocessing import StandardScaler

# 2. scaler 정의 
scaler = StandardScaler()

# 3. train data에 scaler를 fit (학습 데이터에 대해 fit)
scaler.fit(X_train)

# 4. train data 변환 (학습 데이터에 대해 transform)
X_train_scaled = scaler.transform(X_train)

# 5. test data 변환 (학습데이터를 스케일링한 scaler로 테스트 데이터도 transform - fit은 하지 않음)
X_test_scaled = scaler.transform(X_test)

# 번외) fit_transform() 메서드를 쓴다면 
# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)
```

- 학습 데이터에 fit한 설정을 그대로 test set에도 적용하는 것 
- 만약 test set에도 fit을 해버리면 scaler가 기존에 학습 데이터에 fit한 기준을 다 무시하고 test

<br>

- train_test_split을 하기 전에 미리 전처리를 한 후 train, test 분리를 해줘도 무방
  - train_test_split > train, test data 각각 전처리 
  - 전체 데이터에 한해 전처리 > train_test_split 

<br>

### practice

```python
# 필요한 라이브러리 호출 
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandartScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 데이터 load 및 split 
cancer = load_bread_cancer()
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=42)

# 데이터 전처리 
scaler = StandardScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 로지스틱 회귀분석 
log_reg = LogisticRegression(random_state=42)
log_reg.fit(X_train_scaled, y_train)
y_pred = log_reg.predict(X_test_scaled)

# 전처리 했을 때 성능 
print('전처리 o: ', accuracy_score(y_test, y_pred))
>>> 전처리 o: 0.979

# 전처리 안 했을 때 성능
log_reg.fit(X_train, y_train)
y_pred2 = log_reg.predict(X_test)
print('전처리 x: ', accuracy_score(y_test, y_pred2))
>>> 전처리 x: 0.965 
```

- 전처리 하지 않았을 때보다 했을 때 성능이 개선됨 

<br>

```python 
from sklearn.preprocessing import RobustScaler, MinMaxScaler, MaxAbsScaler 

# RobustScaler 
scaler2 = RobustScaler()
X_train_scaled2 = scaler.fit_transform(X_train)
X_test_Scaled2 = Scaler.transform(X_test)

log_reg.fit(X_train_scaled2, y_train)
y_pred2 = log_reg.predic(X_test_scaled2)

# MinMaxScaler
scaler3 = MinMaxScaler()
X_train_scaled3 = scaler.fit_transform(X_train)
X_test_Scaled3 = Scaler.transform(X_test)

log_reg.fit(X_train_scaled3, y_train)
y_pred3 = log_reg.predic(X_test_scaled3)

# MaxAbsScaler
scaler4 = MaxAbsScaler()
X_train_scaled4 = scaler.fit_transform(X_train)
X_test_Scaled4 = Scaler.transform(X_test)

log_reg.fit(X_train_scaled4, y_train)
y_pred4 = log_reg.predic(X_test_scaled4)

# 성능 비교 
print('StandardScaler 성능: ', accuracy_score(y_test, y_pred))
print('RobustScaler 성능: ', accuracy_score(y_test, y_pred2))
print('MinMaxScaler 성능: ', accuracy_score(y_test, y_pred3))
print('MaxAbsScaler 성능: ', accuracy_score(y_test, y_pred4))

>>>StandardScaler 성능: 0.979
>>>RobustScaler 성능: 0.979
>>>MinMaxScaler 성능: 0.979
>>>MaxAbsScaler 성능: 0.979
```
- 해당 데이터의 경우엔 스케일링 방법에 따른 성능차는 없는 것으로 나타남 

---
#### 참고 
@ https://for-my-wealthy-life.tistory.com/18