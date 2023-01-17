# review/views.py
from django.shortcuts import render

# Create your views here.
def index(request):

    # Res => HRML render 
    # render(2. requedts, | 2. HTML | 3. 넘길 데이터)
    return render(request, 'review/index.html')


def hello(request):

    return render(request, 'review/hello.html')