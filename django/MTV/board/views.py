# board views.py
from django.shortcuts import render, redirect
from .models import Posting

# 글 목록화면(read)
def main(request):
    # 글 목록조회 
    # 기본 => id 오름차순 
    # postings = Posting.objects.all()

    # id 내림차순 (python)
    # postings = Posting.objects.all()[::-1] 
    # id 내림차순 (DB)
    postings = Posting.objects.order_by('-pk')
    context = {'postings': postings, }
    return render(request, 'board/main.html', context)

# 글 상세화면
def content(request, posting_pk):
    posting = Posting.objects.get(pk=posting_pk)
    context = { 'posting': posting, }
    return render(request, 'board/content.html', context)

# 글 쓰기화면(creat)
def form(request):
    return render(request, 'board/form.html')

# 글 DB에 실제 저장 
def create(request):
    posting = Posting()
    posting.subject = request.POST['subject']
    posting.description = request.POST['descirption']
    posting.save()
    return redirect('board:content', posting.pk)

# 글 수정화면(update)
def correct(request, posting_pk):
    posting = Posting.objects.get(pk=posting_pk)
    context = { 'posting': posting, }
    return render(request, 'board/correct.html', context)

# 글 DB에 실제 수정 
def update(request, posting_pk):
    posting = Posting.objects.get(pk=posting_pk)
    posting.subject = request.POST['subject']
    posting.description = request.POST['description']
    posting.save()
    return redirect('board:content', posting.pk)

# 글 삭제(delete)
def delete(request, posting_pk):
    if request.method == 'POST':
        posting = Posting.objects.get(pk=posting_pk)
        posting.delete()
    return redirect('board:main')