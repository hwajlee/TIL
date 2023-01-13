from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe

from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# 로그인 한 사람에게만 가능하도록 
@login_required
@require_http_methods(['GET', 'POST'])
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid(): # 체크 과정이 없으면 form.save() 불가능 
            article = form.save(commit=False)
            article.user = request.user # user만 request에서 꺼낼 수 있음
            article.save()
            return redirect('board:article_detail', article.pk)
    else:
        form = ArticleForm()
    context = {'form': form }
    return render(request, 'board/form.html', context)

@require_safe # GET, (HEAD) 요청만 허용하겠다
def article_index(request):
    articles = Article.objects.order_by('-updated_at')
    context = {'articles': articles, }
    return render(request, 'board/index.html', context)

@require_safe
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = CommentForm() # forms.py를 활용해서 detail.html에 input태그 줄이고자
    context = {'article': article, 'form': form, }
    return render(request, 'board/detail.html', context)

@require_POST # 댓글 생성은 DB를 바꾸므로 POST
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk) # 생성하려는 댓글의 주인(게시글)
    form = CommentForm(request.POST)

    if form.is_valid:
        # 완전 저장하려고 하면 Not Null 에러 뜨니까, 직전에 멈춰주세요
        comment = form.save(commit=False) # 이 단계에서 comment.article이 비어있으므로 저장안됨 따라서 저장 직전에 멈춰주세요! 하고 false 값 설정 
        # 나머지는 직접 할게요
        comment.user = request.user
        comment.article = article
        comment.save()
    # 맨 처음에 article = ~ 게시글 지정해줬으므로 redirect에서
    # comment.article.pk가 아니라 article.pk로 써줘도 괜찮음 

    return redirect('board:article_detail', article.pk)

# update_article, delete_article

@login_required
@ require_POST
def delete_comment(request, article_pk, comment_pk): # 뭐가 필요하지? 코멘트 삭제? 삭제하기 위한 최소한의 재료는?
    comment = get_object_or_404(Comment, pk=comment_pk) # 하나만 가져오고 싶으면 무조건 get~ 
    article = get_object_or_404(Article, pk=article_pk) # article_pk 검사 > 믿을만함 ㅇㅋ > 아래 redirect 인자로 넘기기 가능
    if request.user == comment.user: # 요청을 보낸 사용자가 댓글작성자가 아니라면 무시 
        comment.delete()
    return redirect('board:article_detail', article.pk)

@login_required
@require_http_methods(['GET', 'POST'])
def article_update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('board:article_detail', article.pk)
    elif request.user == article.user: 
        form = ArticleForm(instance=article)
    else:
        return redirect('board:article_detail', article.pk)
    context = { 'form': form, }
    return render(request, 'board/form.html', context)


@login_required
@require_POST
def article_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user: 
        article.delete()
    return redirect('board:index')
