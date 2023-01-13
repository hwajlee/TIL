# board/form.py

from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        exclude = ('user', )


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        min_length=2, max_length=200,
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    class Meta:
        model = Comment
        # fields = '__all__'일 경우 예로 1번 article ui에서 4번 article을 선택해서 
        # 댓글 작성이 가능하단 문제 발생 
        exclude = ('article', 'user', ) # class comment 모델에 필드명을 article로 지정했으므로
        # 특정 컬럼을 뺐다는 것은 검정 대상에서도 빠진다는 소리이므로 