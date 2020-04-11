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
    meili = [
        {"name":'水上项目',"path":'/static/img/水上项目/s1.png','jj':'简介','xq':'详情'}
    ]
    context['title'] = '陶瓷水镇旅游官方网站'
    for i in range(11):
        meili.append(meili[0])
    context['meili'] = meili
    #context['hello'] = 'Hello World!'
    return render(request, 'index.html', context)

def test(request):
    context = {}
    return render(request, 'traditional/summary.html',context)
def tradition(request):
    context = {}
    return render(request, 'tradition.html',context)