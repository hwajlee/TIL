## Numpy

- What?

  - **Numerical Computing**: 컴퓨터가 *실수값을 효과적으로 계산*할 수 있도록 하는 연구 분야
  - **Vector Arithmetic**(벡터 연산) => 데이터가 벡터로 표현되기 때문 

  - 행렬이나 일반적으로 다차원 배열을 쉽게 처리할 수 있도록 지원하는 파이썬의 라이브러리 

  - 데이터 구조 외에도 수치 계산을 위해 효율적으로 구현된 기능을 제공함

    

  ![img](https://postfiles.pstatic.net/MjAyMTEwMDZfMTQz/MDAxNjMzNTA3ODg4MDI0.TK4Ec09t6G0wuT1fe_Utg_8cCwm_qsnycmMqq1K90V4g.bAeGD3GjsZcICBwQD0q6cFUtFlz9fXiOhH4eyVO7IUsg.JPEG.swedu_et/What-is-NumPy-in-Python.jpg?type=w966)

  <이미지출처: educba 홈페이지>

  - 기본적으로 array라는 단위로 데이터 관리하며, 이러한 데이터를 활용해 다양한 연산 및 데이터 분석 
  - array에는 데이터의 위치를 표시해주는 좌표인 index라는 개념이 존재 
  - 이를 활용해 특정 데이터를 쉽게 가져올 수 있음(리스트와 유사)
  - Numpy 배열 종류 
    * 1D array(벡터)
    * 2D array(행렬)
    * 3D array(텐서)

- Why?

  * numpy array를 쓰는 가장 큰 이유는 vector처럼 사용할 수 있기 때문

  * 일반 python list(or tuple)과 비슷한데 이에 비해 강력한 성능을 가짐

  * 따라서 다양한 머신러닝 라이브러리들이 numpy에 의존 (ex. scipy, matplotilb, scikit-learn, pandas, tensorflow, pytorch 등 대부분의 분석 라이브러리들은 벡터를 사용하는데, 그 벡터가 바로 numpy array 표현되기 때문에) 

  * pandas, array를 활용해서 분석하고자 하는 데이터를 행과 열을 지닌 데이터 프레임 형태로 가공하여 특정 데이터만 추출하여 EDA하는 데 많이 활용됨 

    ** 이때 pandas는 python data analysisdl 약자로 엑셀 기능 사용 가능 

  * 특징 

    - 여러 데이터를 한번에 다룰 수 있으나 모든 데이터가 동일한 *Data type*을 가져야 함

    - numpy array는 선언 시 크기 지정 후 변경 불가 (복사가 일어나기 때문)

      > 따라서 append 함수가 있기는 하나 list에서 append와는 구별됨

    - 파이썬이 numerical computing에 취약하다는 단점을 보완 

    - *universal function(through broadcast)*를 제공하기 때문에 같은 연산 반복에 대해 훨씬 빠름 (데이터의 크기가 크 수록 차이 大)

      

- How?

##### References

[Numpy 개념](https://ko.wikipedia.org/wiki/NumPy, https://blog.naver.com/swedu_et/222528768698)

[Numpy 특징](https://blog.naver.com/intouchables/222447482675)



