

# Django relational database 

관계형 데이터베이스란 테이블(table)로 이루어져 있으며, 테이블은 키(key)와 값(value)의 관계를 나타낸다.

관계형 데이터베이스의 테이블(table)은 다음 그림처럼 구성된다. 

 ![코딩의 시작, TCP School](https://www.tcpschool.com/lectures/img_mysql_table.png)

##### 관계형 데이터베이스의 특징 

1. 데이터 분류, 정렬, 탐색 속도가 빠르다.   

2. 오랫동안 사용된 만큼 신뢰성이 높고, 어떤 상황에서도 데이터의 무결성을 보장해 준다. 

3. 기존에 작성된 스키마를 수정하기 어렵다. 

4. 데이터베이스의 부하를 분석하는 것이 어렵다. 

   

##### 관계(relationship)

1. 일대일(one-to-one) 관계

2. 일대다(one-to-many) 관계

3. 다대다(many-to-many) 관계 

   

![테이블 간의 관계](http://www.tcpschool.com/lectures/img_mysql_relationship.png)

출처: TCP school



---



# Project RECAP 

- one-to-many 

- table 구성 

  | User |          |          |      |
  | ---- | -------- | -------- | ---- |
  | id   | username | passowrd | mbti |
  | 1    | neo      | 1234     | infp |
  | 2    | justin   | 4434     | enpj |
  | 3    | alex     | 2898     | estp |
  | 4    | kyle     | 12314    | istp |
  | PK   |          |          |      |

  | Question |              |         |
  | -------- | ------------ | ------- |
  | id       | title        | user_id |
  | 1        | 오늘 점심은? | 1       |
  | 2        | 회식 메뉴    | 2       |
  | 3        | 간식 종류    | 3       |
  | 4        | 점메추       | 2       |
  | PK       |              | FK      |

  | Reply |          |      |             |         |
  | ----- | -------- | ---- | ----------- | ------- |
  | id    | content  | vote | question_id | user_id |
  | 1     | 닭칼국수 | 10   | 1           | 3       |
  | 2     | 치킨     | 2    | 1           | 4       |
  | 3     | 스테이크 | 2    | 2           | 4       |
  | 4     | 햄버거   | 40   | 3           | 2       |
  | PK    |          |      | FK          | FK      |

  회원가입을 한 user가 게시판 글 및 댓글 작성을 할 수 있도록 서버 구현 

  +댓글 추천(vote) 기능 추가

  

  ##### Project setting 

  ```python
  - git bash 열기 
  mkdir RECAP # 폴더 생성 
  pyhon -m venv venv # 가상환경 생성 
  - vs code 터미널 
  source venv/Scripts/activate 
  # 콘솔 바뀌는 지 확인
  # 위 실행어 입력 혹은 ctril + ship + s -> 인터프리터에서 venv 지정해줄 것 
  pip install django==3.2.16 django_extensions 
  pip freeze > requirements.txt 
  touch .gitignore README.md 
  django-admin startproject recap . 
  # gitignore.io에서 #python #django #venv 입력 후 코드 복붙 
  mkdir templates 
  touch templates/base.html 
  python manage.py startapp polls 
  cd polls/
  touch urls.py forms.py 
  mkdir -p templates/polls
  cd templates/polls/
  touch question_form.html question_index.html question_detail.html
  cd- 
  cd ..
  python manage.py startapp accounts
  cd accounts/
  touch urls.py forms.py
  mkdir -p templates/accounts
  cd templates/accounts/
  touch login.html signup.html
  cd- 
  cd ..
  ```

  - settings.py 

    - TEMPLATES [BASE_DIR / 'templates']

    - INSTALLED_APPS = ['django_extensions', 'polls', 'accounts']

    - 언어 ko-kr로 변경 

      

  - 마스터 urls.py에서 path 지정 

    ```python
    from django.contrib import admin
    from django.urls import path, include
    
    def to_main(request):
        from django.shortcuts import redirect
        return redirect('polls:question_index')
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('accounts/', include('accounts.urls')),
        path('polls/', include('polls.urls')),
        path('', to_main)  
    ```

    

