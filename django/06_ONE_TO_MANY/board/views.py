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
    from django.db.models import Count
    # Article 테이블에 가상의 컬럼을 만들어(annotate), 
    # 컬럼 이름은 like_count고, 
    # like_users를 count해서 채울 것이며, 
    # 이 가상의 컬럼을 기준으로 내림차순 정렬하겠다. (좋아요 개수 기준으로 정렬)
    articles = Article.objects.annotate(like_count=Count('like_users')).order_by('-like_count')
    context = {'articles': articles, }
    return render(request, 'board/index.html', context)

@require_safe
def article_detail(request, article_pk):
    # article 상세 페이지
    article = get_object_or_404(Article, pk=article_pk)
    # 댓글 입력 창 => _comment_form.html
    form = CommentForm() # forms.py를 활용해서 detail.html에 input태그 줄이고자
    # 좋아요 버튼 UI 결정 Flag
    is_like = article.like_users.filter(pk=request.user.pk).exists()
    context = {'article': article, 'form': form, 'is_like': is_like,}
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
def update_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 작성자 아니면 돌려보내기
    if request.user != article.user:
        return redirect('board:article_detail', article.pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)        
        if form.is_valid():
            # 기존에 저장된 user_id 갱신할 필요가 없기때문에 commit=False 필요 X
            article = form.save()
            return redirect('board:article_detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {'form': form}
    return render(request, 'board/form.html', context)
'''
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
'''

@login_required
@require_POST
def delete_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user: 
        article.delete()
        return redirect('board:article_index')
    else:
        return redirect('board:article_detail', article.pk)


# /board/1/like/ 
@login_required
@require_POST
def like_article(request, article_pk):
    # 게시글 하나/사용자 하나 
    # user가 특정 게시글을 좋아요 한다!
    # u1.like_articles.add(a1)
    # a1.like_users.add(u1)
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user
    # article에 좋아요 한 사람들 중에, user가 있나요?
    # if user in article.like_users.all() => 효율 안 좋음 이 코드보단 아래 코드가 나음 
    is_like = article.like_users.filter(pk=user.pk).exists()

    # 기존에 좋아요를 했으면 
    if is_like:
        # 좋아요 테이블에서 삭제
        user.like_articles.remove(article)
    # 아니라면 
    else:
        # 좋아요 테이블에 추가 
        user.like_articles.add(article)
    return redirect('board:article_detail', article.pk)