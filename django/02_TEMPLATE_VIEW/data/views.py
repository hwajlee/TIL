# data/views.py 
from django.shortcuts import render

def index(request):
    print('This is data index')
    return render(request, 'data/index.html')

def hello(request, name):
    context = {'name': name}
    return render(request, 'data/hello.html', context)

def user_input(request):
    return render(request, 'data/user_input.html')

def user_output(request):
    c = int(request.POST['cel']) # request 안에서 섭씨데이터 꺼내기 
    f = c * 1.8 + 32

    context = {
        'f': f, 
        'username' : request.POST['username'],
        'password' : request.POST['password'],
    }
    
    return render(request, 'data/user_output.html', context)

