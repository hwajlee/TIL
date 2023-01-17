from django.db import models

# Create your models here.

class Article(models.Model):
    # id(고유값)는 django에서 자동으로 만들어줌
    # CharField => 짧은 str  
    author = models.CharField(max_length=30) # (max_length = ) 길이 제한  
    title = models.CharField(max_length=100)
    # TextField => 긴 str 
    content = models.TextField() 
    
    # tttt = models.IntergerField(default=0) # 열추가시 null값이 들어가면 안되므로 디폴트값 지정 필요 
# class Article() 여기까지 하면 아직 실제 데이터베이스에 반영된 것 아님 
# 따라서 ()괄호 안에 상속받은 뒤 
# 'python manage.py makemigrations board'

# 1. models.py 작성 및 수정 
# 2. python manage.py makemigrations board *이때 boadr는 <app_name>
# 3. python manage.py migrate <app_name> 



