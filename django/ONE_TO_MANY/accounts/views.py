# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.http import require_http_methods

@ require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('board:article_index')

    else:
        form = UserCreationForm()
    context = {'form': form }
    return render(request, 'accounts/signup.html', context)

@ require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        # 다른 form과 인자 구성이 다름(다른 form과는 달리 인증폼은 첫번째 인자가 request )
        form = AuthenticationForm(request, request.POST) 
        if form.is_valid():
            user = form.get_user() # 유저 개체 가져오기
            auth_login(request, user)
            # None / URI string
            next = request.GET.get('next')
            return redirect(next or 'board:article_index')
    else: 
        form = AuthenticationForm()
    context = {'form': form }
    return render(request, 'accounts/login.html', context)



def logout(request):
    auth_logout(request)
    return redirect('board:article_index') 