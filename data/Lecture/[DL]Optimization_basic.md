## Optimization basic 
---
- Gradient Descent 과정에서 데이터가 많아지고, 신경망이 복잡해질 수록, 한 번만의 계산으로 최적화된 값을 찾는 것을 매우 힘든 일 
- 따라서 딥러닝에서 최적화(Optimization)을 할 때는 일반적으로 여러 번 학습 과정을 거치는 데, 여기서 Epoch, Batch size, Iteration이라는 개념 등장 

<br>

### Epoch, Step 
- Epoch: 전체 데이터 셋에 대해 Forward pass, Backword pass 과정을 통해 **한 바퀴 돌며 학습하는 것**을 의미 
- 순방향 패스(Forward pass): 신경망에서 역전파 알고지름을 사용할 때 입력부터 출력까지 각 계층의 Weight를 계산하는 과정 
- 역방향 패스(Backword pass): 반대로 거슬러 올라가며 기존의 Weight를 수정하는 과정 
- 이 둘을 합치면 Epoch 
- 모델을 만들 때 적절한 Epoch를 사용해야 underfitting과 overfitting을 방지 가능 
- Step: Epoch 과정에서 Weight와 Bias를 1회 업데이트 하는 것을 1 Step이라고 부름 

<br>

### Batch size, Iteration 
- Batch size: 한 번의 Batch마다 주는 데이터 샘플의 size(크기)를 의미
- Iteration: Epoch를 나누어서 실행하는 횟수
    - ex) 총 데이터 = 100개, batch size = 10 
    - 1 iteration = 10개의 데이터에 대해 학습하는 것 
    - 1 Epoch = 10 iteration 
- Epoch를 iteration으로 나누는 이유는 메모리의 한계와 속도 때문 

<br>

#### Batch size 조절 과정 
- Batch size를 줄일 수록 필요한 메모리가 감소하며, 그에 따라 학습의 속도가 향상됨 (똑같은 데이터를 여러 번 나누어서 weight 갱신을 여러 번 하기 때문)
- Batch size 늘릴 수록 Gradient의 평가 정확도가 올라가며, overfitting 방지 효과 有

---
#### 참고자료 
@ https://m.blog.naver.com/sjc02183/221768995624