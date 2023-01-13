from django.shortcuts import render

# Create your views here.
def info(request):
    return render(request, 'saju/info.html')

def result(request):
    return render(request, 'saju/result.html')