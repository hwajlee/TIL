### 분류 모델의 평가지표
---

- ML 문제의 큰 범주 
  - 분류 (Classification): 예측해야 할 대상의 개수가 정해져 있는 문제 
    ex) 이미지에서 개, 고양이 분류 
  - 회귀 (Regression): 예측해야 할 대상이 연속적인 숫자인 문제 
    ex) 일기 예보에서 내일의 기온 예측 

> 해결하고자 하는 문제의 목적에 맞게 평가지표를 설정해야 모델 성능을 제대로 평가할 수 있고, 이를 기준으로 모델 성능 고도화 가능! **분류모델에서 흔히 사용되는 평가 지표는?**

<br>



### 혼동 행렬(Confusion Matrix)
---

|                         | 예상(예)         | 예상(아니오)    |
| ----------------------- | ---------------|-----------------|
| 실제(예)                 | TP             | FN            |
| 실제(아니오)             | FP             | TN            |


- 실제 클래스와 예측된 클래스의 매칭을 이용하여 분류 모델을 평가하는 도구 
  
    **분석가가 더 관심이 있는 범주, 즉 관심범주에 따라서 예를 잘 예측하는 것이 중요한지 B를 더 잘 예측하는지를 중요한지는 분석가의 의도에 달렸다.** (TP, TN의 숫자가 많을 수록 좋은 모델이지만 TP와 TN 중 어디에 더 초점을 둘 것이냐의 문제는 존재)
- 발생 가능한 네 가지 경우 
  
  만약 관심범주가 '예'라면? 
    1) TP(True Positive): 관심범주를 정확하게 분류 
    2) FP(False Positive): 관심범주로 잘못 분류
    3) FN(False Negative): 관심범주가 아닌 것으로 잘못 분류 
    4) TN(True Negative): 관심범주가 아닌 것을 정확히 분류 
   
<br>


### Accuracy, Percision, Recall
---

<예시 표>
1. A병원 

| 실제값                           | 예측값         |                  |
| ------------------------------- | ---------------|----------------- |
|                                 | 암환자          | 일반환자         |
| 암환자                          | 9               | 1                |
| 일반환자                        | 30              | 60               |

2. B병원 

| 실제값                           | 예측값         |                  |
| ------------------------------- | ---------------|----------------- |
|                                 | 암환자          | 일반환자         |
| 암환자                          | 1               | 9                |
| 일반환자                        | 20              | 70               |


<br>


#### `정확도(Accuracy)`


<br>

- Accuracy: 판별한 전체 샘플 중 TP와 TN의 비율로 모델이 입력된 데이터에 대해 얼마나 정확하게 예측하는 지를 나타냄 
  > Accracy = $\frac{TP + TN}{TP + FP + FN + TN}$ 
  = 예측값 결과와 실제값이 동일한 건수 / 전체 데이터 수 
  
- ex) 
  - A 병원의 정확도 = (9+60)/(9+60+1+30) = 0.69
  - B 병원의 정확도 = (1+70)/(1+70+9+20) = 0.71
  > **정확도는 B병원이 높지만 암을 기준으로 하면 B가 더 안좋다.** 암환자만 따로 떼어놓고 보면 암환자가 실제로 10명(9+1) 존재하는데 1명만 암환자로 예측했다. 

- 장점: 분류 모델을 평가하기에 가장 단순한 지표 
- 단점: 불균형한 클래스를 가진 데이터 셋을 평가하기 어려움 

<br>


#### `정밀도(Precision)`

- Precision: 분류 모델이 Positive로 판정한 것 중, 실제로 Positive인 샘플의 비율로 Positive로 검정된 결과가 얼마나 정확한 지를 나타냄(f=PPV, Positive Predictive Value)
  쉽게 말해 '예'라고 예측했을 때의 정답률 
  > Precision = $\frac{TP}{TP + FP}$

- ex)
  - A병원의 암환자 정밀도 = 9/(9+30) = 0.23
  - B병원의 암환자 정밀도 = 1/(1+20) = 0.04
  **정확도는 B모델이 높지만 정밀도는 A모델이 높다.**

#### `재현율(Recall)`
- Recall: 실제 Positive 샘플 중 분류 모델이 Positive로 판정한 비율(=Sensitivity(민감도), TPR(True Positive Rate, 양성률))
- Recall은 분류 모델이 실제 Positive 클래스를 얼마나 빠지지 않고 잘 잡아내는 지를 나타내므로 주요 지표 
- 실제 암환자들이 병원에 갔을 때 암환자라고 예측될 확률, 조기에 정확하게 발견해서 신솔하게 처방하는 것이 올바른 모델 
  > Recall = $\frac{TP}{TP + FN}$

- ex)
  - A병원의 암환자 재현율 = 9/(9+1) = 0.9
  - B병원의 암환자 재현율 = 1/(1+9) = 0.1
  > **암환자 재현율을 기준으로 더 나은 모델은 A모델이다.**

### Precision-Recall 관계
---
#### `F1-score`
- F1-score: Precision과 Recall의 조화평균으로 1에 가까울 수록 분류 성분이 좋음 (0<F1-score<1)
  
  정밀도 중요하고 재현율도 중요한데 둘 중 무엇을 쓸지 고민될 경우 두 값을 조화평균내서 하나의 수치로 나타낸 지표
  > F1-score = $2*\frac{Precision * Recall}{Precision + Recall}

- ex)
  - A병원의 F1점수 = 2*0.9*0.23/(0.9+0.23) = 0.69
  - B병원의 F1점수 = 2*0.1*0.04/(0.1+0.04) = 0.14
  
- Precision-Recall Curve
  > Trade-off 관계: Precision이 올라가면 Recall이 떨어지고 Recall이 올라가면 Precision이 떨어짐
  
  > Decision threshold를 통해 trade-off 관계 조절 가능 (*Decision threshold: 분류 모델의 결과인 [0, 1] 사이의 값을 positive 또는 negative로 결정하는 경계) 
![](./Image/정밀도와재현율.png)

  > Precision-recall curve(우측 그래프의 경우 Precision과 Recall 값을 threshold 변화에 따른 그래프로 나타낸 것)
  ![](./Image/curve.png)

### 그 외 분류 성능 지표 
---
#### `Error Rate`
- Error Rate(오분류율): 모델이 전체 데이터에서 잘못 맞춘 비율 
  > Error Rate = $\frac{FP + FN}{TP + TN + FP + FN}$

  <br>


#### `TNR(True Negative Rate)`
- TNR(특이성): 실제 Negative 샘플 중 분류 모델이 Negative로 판정한 비율로 Specificity(특이도) 또는 Selectivity라고도 불림 (Recall과 반대 개념)
  
  <br>


  > TNR = $\frac{TN}{FP + TN}$
#### `FPR(False Positive Rate)`
- FPR(위양성률): 실제 Negative 샘플 중 분류 모델이 positive로 판정한 비율
  > FPR = $1 - TNR1$ = $\frac{FP}{FP + TN}$

  <br>


#### `ROC Curve`
- ROC(Receiver Operating Characteristic) curve: threshold에 따른 TPR과 FPR(=Fall-out)을 나타낸 그래프로 대각선을 기준으로 좌상단에 붙어 있는 ROC curve일 수록 좋은 분류 성능 나타냄

  - y축: 정답이 1인 케이스에 대해 1로 잘 예측하는 비율(TPR = $\frac{TP}{FN + TP}$) 
  - X축: 정답이 1인 케이스에 대해 잘못 예측한 비율(FPR = $\frac{FP}{TN + FP}$)
  - 모델의 임계값(Cutoff Value)를 변경시켜가며 그린 곡선을 나타냄 
  > ![](./image/TPR%26FPR.png) 
  출처: 부스트코스

  > ![](./Image/roc_curve.png)
  
  > ROC-AUC (Area Under the Curve) = ROC curve의 면적

- AUC 
  - ROC 곡선 아래 영역 
  - 0~1 사이의 값을 가짐
  - 1에 가까울 수록 모델이 잘 예측하는 것을 의미

#### Reference
- 분류 성능 지표 
  
  @ https://en.wikipedia.org/wiki/Confusion_matrix

  @ https://ai-com.tistory.com/entry/ML-%EB%B6%84%EB%A5%98-%EC%84%B1%EB%8A%A5-%EC%A7%80%ED%91%9C-Precision%EC%A0%95%EB%B0%80%EB%8F%84-Recall%EC%9E%AC%ED%98%84%EC%9C%A8
  
  @ https://white-joy.tistory.com/9?category=1015070
  @ https://truman.tistory.com/179