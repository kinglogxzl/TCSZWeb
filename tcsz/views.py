from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):         #request参数必须有，名字类似self的默认规则，可以修改，它封装了用户请求的所有内容
    #return HttpResponse("Hello world ! ")
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

def index(request):
    context = {}
    #context['hello'] = 'Hello World!'
    return render(request, 'index.html', context)

def test(request):
    context = {}
    #context['hello'] = 'Hello World!'
    return render(request, 'index2.html', context)