## 머신러닝의 종류 

## 지도학습(Supervised learning)

### 분류 
- Decison Tree(의사결정나무)
- Logistic Regression(로지스틱회귀)
- Naive Bayes(나이브베이지안)
- KNN(K-Nearest Neighbor)
- Random Forest(Tree Based)
- Support Vector Machine
- XGBoost(Tree Based)
- LightGBM(Tree Based)

<br>

### 회귀
- Linear Regression(Stepwise)
- Regularized Linear Regression
- Regression Tree
- KNN(K-최근접 이웃)
- Random Forest(Tree-Based)
- Support Vector Machine
- XGBoost(Tree Based)
- LightGBM(Tree Based)

<br>

## 비지도학습(Unsupervised learning)

### 차원축소 
- PCA(주성분분석)
- Factor Analysis(요인분석)
- MDS(다차원척도법)

<br>

### 군집화
- Hierarchical Clustering
- K-means Clustering
- K-medoids Clustering
- SOM(자기조직화지도)

<br>

- MBA(장바구니분석)
- Sequence MBA(순차장바구니)
- Collaborative Filtering(협업필터링 추천시스템)

<br>

---

## 머신러닝의 분석 프로세스 

### 분석 준비 

- 1. Data Set 분할 
  - 주요 과제
    - 학습 데이터를 랜덤으로 학습/검증 셋(train/validation) 분할
    - 테스트 셋(test)도 준비 
  - 실전 전략
    - 학습 데이터: 70~90%
    - 검증 데이터: 10~20%
    - 테스트 데이터: 10~20%
    - 학습 데이터를 그룹으로 나누어서 교차 검증을 하는 방법도 추천 

<br>

- 2. 데이터 전처리 
  - 주요 과제
    - 데이터의 표준/정규화 
    - 범주자료 one-hot encoding 
    - 특성변수의 축약 
  - 실전 전략 
    - 표준화(평균 0 / 표준편차 1) 또는 Min-Max 정규화
    - 범주형 특성변수를 0과 1의 값으로 변환 
    - 고차원의 경우 PCA 방법 등으로 차원 축소 

<br>

### 모델평가 및 결정 

- 3. 모델 적용 
  - 주요 과제
    - 과제 해결에 적합한 머신러닝 알고리즘 적용 
    - 평가지표를 통한 모델 평가 
  - 실전 전략
    - 예측/분류/비지도 알고리즘에 데이터 학습 
    - 학습된 모델에 검증 데이터로 평가 
    - 정확도 및 과소/과대추정 여부 판단 
    - 파라미터 조정을 통한 최적 모델 결정 

<br>

- 4. Hyper Parameter 탐색 및 결정 
  - 주요 과제
    - 다양한 하이퍼 파라미터 적용 
    - 최적의 Hyper Parameter 및 모델 결정 
  - 실전 전략 
    - 최종 분류기에서 검증 셋은 사용하지 않는 것이 좋음 
    - 최종 모델을 테스트 셋에 대해 성능을 평가 
    - 테스트 셋에 대한 정확도를 현재 데이터로 학습한 알고리즘 성능으로 제시