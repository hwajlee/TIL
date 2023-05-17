## Underfitting & Overfitting
---
- Fit이라는 표현은 데이터를 잘 설명할 수 있는 능력을 의미 
- Underfitting은 데이터를 잘 설명하지 못하는 상황을 뜻하며, Overfitting은 반대로 데이터를 과도하게 설명하는 상황 
- 모델링의 목적은 보유하고 있는 데이터를 잘 분석해 전체 데이터, 혹은 새로운 데이터에 대해서도 잘 표현해주는 모델을 만드는 것이므로 Overfitting을 제어하고 방지해줘야 함  
  - 모델이 Noise 데이터에 민감하지 않도록 규제하는 방법인 Regularization 방법이 있으며, Regularization을 시도할 수 있는 다양한 방법들이 존재 (아래에서 자세히 설명)
  

<br>

![](./Image/overfitting.png)
![](./Image/model_complexity.png)
- Model's Capacity가 극대화 되면서 학습 오차(training error)가 일반화 오차(generalization error)에 비해 현격하게 낮아지는 현상
- 다시 말해 train data에 한해서는 높은 정답률을 보이지만 test data에 대해서는 낮은 정답률을 보이므로 overfitting을 주의해야 한다.

<br>

### Regulrization for Deep Learning 
- lan Goodfellow의 <Deep Learning> 책의 Chp7. Regulrization for Deep Learning 
- 머신러닝에서 주요 문제는 '학습셋뿐만 아니라 새로운 데이터 또한 어떻게 잘 맞추는가' 
- 이 문제에 답하기 위해서는 오버피팅을 해결해야 하며, 가장 효과적인 해결책은 **정규화**
- 이때 정규화는 training error를 줄이는 게 아닌, generalization error(train error - test error)를 감소시키기 위한 것이라고 책에서 정의함 


<br>

## Avoiding overfiting
---

### 1. Early Stopping 

![](./Image/early_stopping.png)

- 정형데이터 분석에서의 Early Stopping 방식은 딥러닝에서의 방식과 유사 
- Training data를 Train set과 Validation set으로 나눈 뒤, Train set으로 학습을 진행하며 Validation set에서의 성능을 지속적으로 관찰하는 방법 
- Validation Error가 지속적으로 증가하는 지점에서 모델 학습 중단

<br>

### 2. Parameter Norm Penalty 

![](./Image/parameter~.png)

출처: 부스트코스 머신러닝 기본 개념 소개(1)

- 마찬가지로 정형데이터에 적용 가능
- L1과 L2에 대해서 Penalty를 부여할 수 있는 데, L1 penalty를 적용한 그래프인 파란색 선이 적절하게 fitting된 것을 확인 가능 
- 반명 penalty를 적용하지 않은 녹색 그래프는 Overfitting이 발생함 

<br>

### 3. Dataset Augmentation 
- 머신러닝에서 가장 효과적인 정규화 방법은 학습셋의 크기를 늘리는 것 (이때 우리가 가지고 있는 데이터의 수는 제한적이기 때문에 학습셋에 가짜 데이터 포함 가능)
- 주의사항: 학습셋 크기를 늘리기 위해 데이터를 변환할 때, 데이터의 특징을 고려해야 함
  - ex) b와 d, 6과 9처럼 180도를 뒤집은 것 같은 데이터의 경우 좌우 반전하여 데이터를 늘리는 것은 적절치 X 
- Augmentation 하는 방법 
  - 이미지 반전 
  - 이미지 밝기 조절 
  - 서브 샘플링(Subsampling)
  - 노이지(noise) 넣기 

### 4. SMOTE 
![](./Image/Smote.png)

- 정형 데이터에서는 주로 SMOTE라는 기법을 통해 Data Augumentation과 같은 효과를 만들어냄 
- Smote는 Imbalanced된 데이터에서 Minority한 data를 활용해 사이사이 데이터를 생성하는 방식을 사용 
- 즉, 데이터 증강을 통해 Overfitting 방지하는 방법 

<br>

### 5. Dropout (2012, Geoffrey Hinton)

- What? 
  - 신경망에 적용할 수 있는 Overfitting 방법 중 하나 
  - Training을 진행할 때 매 Batch마다 Layer단위로 일정 비율만큼 Neuron을 끄는 방식
  - Test / Inference 단계에서는 Dropout을 하지 않고, 전체 Neuron이 살아있는 채로 Inference 진행
  - **동일한 데이터에 대해 매번 다른 모델을 학습시키는 것과 마찬가지의 효과 발생(일종의 Model ensemble 효과)**

- Example 
  
![](./Image/exam.png)

  - 예를 들어서 고양이 이미지를 10 * 10 으로 100개 퍼셉트로 만들어서 이미지 구조를 파악한 후(고양이 눈, 코, 입) 그 이미지가 어떤 이미지에 접근한 것인지는 알 수 있다.
  
![](./Image/exam2.png)
  
  - dropout을 통해 고양이 이미지를 눈, 입만 보여주고, 코, 꼬리는 안 보여주는 방식으로 학습 가능하다.

![](./Image/exam3.png)

  - 이때 랜덤하게 Neuron을 꺼뜨려 학습을 방해함으로써 모델의 학습이 Training data에 편향되는 것을 막아준다.
  - 그 결과 Training data에 편향되지 않고 Test data에서도 성능을 높일 수 있다.

- How? 
  
![](./Image/dropout2.png)  

![](./Image/dropout.png)

  - 2012년 ImageNet Challenge에서 우승한 Alexnet은 마지막 2개의 Fully-connected layer에 Dropout을 적용하였다. 
  - 이처럼 Dropout은 보통 모든 layer에 적용하는 것이 아니라 마지막 1-2개 layer에 한해서만 적용하며, Dropout 결과 가중치 값이 큰 특정 Neuron의 영향력이 커져 다른 Neuron들의 학습 속도에 문제를 발생시키는 **Co-adaptation**을 회피할 수 있게 해준다. 
  - 따라서 전반적으로 Overfiting을 줄여주므로 Test data에 대한 에러를 더욱 낮출 수 있게 해준다. 
  
![](.Image/../Image/withdropout.png)



### 6. Batch Normalization (2015)
- What?
  
![](./Image/BN.png)

  - Input data에 대해 Standardization과 같은 Normalization을 적용하면 전반적으로 model의 성능이 높아지는 것
  - 데이터 내 Column들 간의 수치 차이가 클 경우 해당 값이 큰 Column에 의해 model이 민감해질 수 있기 때문에 Scale을 통해 조정 필요
  - 신경망의 경우 Normalization이 제대로 적용되어 있지 않으면 **최적의 cost 지점으로 가는 길을 빠르게 찾지 못한다.**
  - 매 layer마다 정규화를 진행하므로 가중치 초기값에 크게 의존하지 않으며, Overfiting을 억제해줌과 더불어 학습 속도 및 학습 결과가 개선되므로 Dropout, L1/L2 regularization보다 더 많이 활용된다. 

- How? 
  
![](./Image/BN2.png)

  - Standardization과 같은 모델은 input data뿐만 아니라 신경망 내부의 중간에 있는 Hidden layer로의 input에도 적용하는 것이 Batch Normalization이다.
  
![](./Image/BN3.png)

  - 각 Hidden layer로의 Input data에 대해 평균이 0, 분산이 1이 되도록 Normalization을 진행 후 Hidden layer의 출력 값이 비선형성을 유지할 수 있도록 Scaling & Shifting을 적용한다.
  - 그 결과를 Activation function에 전달하여 Hidden layer의 최종 output을 계산한다. 
  
![](./Image/BN4.png)

  - Activation function을 적용하기 전에 Batcj normalization을 먼저 적용해준다. 



#### Reference
image source @ https://j.mp/3eAcuu7, @ 부스트코스 쇼핑데이터를 활용한 머신러닝 중 머신러닝 기본 개념 소개(1)

개념 참고 @ https://wegonnamakeit.tistory.com/9
