from board.models import Article

# python manage.py shell
# Article() 한 줄을 활성화 (id, 제목, 작성자, 날짜, 내용이 들어간 하나의 행 )

# create
article = Article()
article.title = '첫번째 글'
article.content = '1빠'
article.author = 'hj'
article.save()

#2. 
article = Article(title='2번글', content='까비', author='김재석')
article.save()

#3. 
Article(title='3번글', content='3등', author='이땡땡').save()

#4. 
Article.objects.create(title='4번글', content='4등', author='호잇')

## Read / Retrieve (조회)
Article.objects # objects 일종의 관리자 
# 단일조회
Article.objects.get(id=1)
article = Article.objects.get(id=1) # article이라는 변수에 저장 후 접근 
article.id # article.pk와 동일 (id=pk)
article.title 
article.content
article.author

# 전체조회 
Article.objects.all() # 모든 객체 불러오라는 뜻 
articles = Article.objects.all()
for article in articles:
    print(article.titles)

# Update(수정)
article = Article.objects.get(id=3) # 먼저 수정할 게시글 고르고, 
article.title = '수정한 글'
article.content = '바뀌어라얍'
article.save()
## 이때 id는 수정 불가능 

# Delete / Destroy (삭제)
article = Article.objects.get(id=3)
article.delete()

