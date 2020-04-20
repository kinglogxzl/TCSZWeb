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
        {"name":'五彩灯笼',"path":'/static/img/水上项目/7.jpg','jj':'','xq':'详情'},
        {"name": '庭院一角', "path": '/static/img/水上项目/2.jpg', 'jj': '', 'xq': '详情'},
        {"name": '古镇门楼', "path": '/static/img/水上项目/11.jpg', 'jj': '', 'xq': '详情'},
        {"name": '水镇夜景', "path": '/static/img/水上项目/3.jpg', 'jj': '', 'xq': '详情'},
        {"name": '水镇夜景', "path": '/static/img/水上项目/10.jpg', 'jj': '', 'xq': '详情'},
        {"name": '水上项目', "path": '/static/img/水上项目/9.jpg', 'jj': '', 'xq': '详情'},
        {"name": '水边民宿', "path": '/static/img/水上项目/1.jpg', 'jj': '', 'xq': '详情'},
        {"name": '水上古船', "path": '/static/img/水上项目/8.jpg', 'jj': '', 'xq': '详情'},
        {"name": '石太铁路', "path": '/static/img/水上项目/6.jpg', 'jj': '', 'xq': '详情'},
        {"name": '景区远景', "path": '/static/img/水上项目/5.jpg', 'jj': '', 'xq': '详情'},
        {"name": '景区俯景', "path": '/static/img/水上项目/4.jpg', 'jj': '', 'xq': '详情'},
        {"name": '河中小岛', "path": '/static/img/水上项目/12.jpg', 'jj': '', 'xq': '详情'}
    ]
    context['title'] = '陶瓷水镇旅游官方网站'
    for i in range(0):
        meili.append(meili[0])
    context['meili'] = meili
    #context['hello'] = 'Hello World!'
    return render(request, 'index.html', context)

def test(request):
    context = {}
    return render(request, 'traditional/summary.html',context)

def tradition(request):
    context = {}
    context['title'] = '水镇概述'
    return render(request, 'watertown/tradition.html',context)
def origin(request):
    context = {}
    context['title'] = '水镇渊源'
    return render(request, 'watertown/origin.html',context)
def celebrity(request):
    context = {}
    context['title'] = '水镇名人'
    return render(request, 'watertown/celebrity.html',context)
def custom(request):
    context = {}
    context['title'] = '水镇民俗'
    return render(request, 'watertown/custom.html',context)
def activity(request):
    context = {}
    context['title'] = '景区活动'
    return render(request, 'activity/activity.html',context)
def new(request):
    context = {}
    context['title'] = '新闻动态'
    return render(request, 'activity/new.html',context)
def notice(request):
    context = {}
    context['title'] = '景区公告'
    return render(request, 'activity/notice.html',context)

def accommodation(request):
    context = {}
    context['title'] = '住宿'
    context['cont'] = [
        {
            'src1': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp.jpg',
            'src2': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp%20(1).jpg',
            'name': '帝师客居宅',
            'intro': ' 陶瓷水镇紧邻甘陶河，风光秀美，人杰地灵，在甘陶河上有北方少见的画舫，乌篷船，和脚踏船，游完古村落，可以乘坐游船，吹吹河风，歇歇脚，遥看整个古村落的全貌。伴随悠扬的音乐，坐在画舫之中，仿佛穿越回千年前的梦里水乡。'
        },
        {
            'src1': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp.jpg',
            'src2': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp%20(1).jpg',
            'name': '帝师客居宅',
            'intro': ' 陶瓷水镇紧邻甘陶河，风光秀美，人杰地灵，在甘陶河上有北方少见的画舫，乌篷船，和脚踏船，游完古村落，可以乘坐游船，吹吹河风，歇歇脚，遥看整个古村落的全貌。伴随悠扬的音乐，坐在画舫之中，仿佛穿越回千年前的梦里水乡。'
        },
        {
            'src1': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp.jpg',
            'src2': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp%20(1).jpg',
            'name': '帝师客居宅',
            'intro': ' 陶瓷水镇紧邻甘陶河，风光秀美，人杰地灵，在甘陶河上有北方少见的画舫，乌篷船，和脚踏船，游完古村落，可以乘坐游船，吹吹河风，歇歇脚，遥看整个古村落的全貌。伴随悠扬的音乐，坐在画舫之中，仿佛穿越回千年前的梦里水乡。'
        },
        {
            'src1': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp.jpg',
            'src2': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp%20(1).jpg',
            'name': '帝师客居宅',
            'intro': ' 陶瓷水镇紧邻甘陶河，风光秀美，人杰地灵，在甘陶河上有北方少见的画舫，乌篷船，和脚踏船，游完古村落，可以乘坐游船，吹吹河风，歇歇脚，遥看整个古村落的全貌。伴随悠扬的音乐，坐在画舫之中，仿佛穿越回千年前的梦里水乡。'
        }
    ]
    return render(request, 'vacation/accommodation.html',context)

def food(request):
    context = {}
    context['title'] = '美食'
    context['cont'] = [
        {
            'src1': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp.jpg',
            'src2': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp%20(1).jpg',
            'name': '帝师客居宅',
            'intro': ' 陶瓷水镇紧邻甘陶河，风光秀美，人杰地灵，在甘陶河上有北方少见的画舫，乌篷船，和脚踏船，游完古村落，可以乘坐游船，吹吹河风，歇歇脚，遥看整个古村落的全貌。伴随悠扬的音乐，坐在画舫之中，仿佛穿越回千年前的梦里水乡。'
        },
        {
            'src1': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp.jpg',
            'src2': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp%20(1).jpg',
            'name': '帝师客居宅',
            'intro': ' 陶瓷水镇紧邻甘陶河，风光秀美，人杰地灵，在甘陶河上有北方少见的画舫，乌篷船，和脚踏船，游完古村落，可以乘坐游船，吹吹河风，歇歇脚，遥看整个古村落的全貌。伴随悠扬的音乐，坐在画舫之中，仿佛穿越回千年前的梦里水乡。'
        },
        {
            'src1': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp.jpg',
            'src2': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp%20(1).jpg',
            'name': '帝师客居宅',
            'intro': ' 陶瓷水镇紧邻甘陶河，风光秀美，人杰地灵，在甘陶河上有北方少见的画舫，乌篷船，和脚踏船，游完古村落，可以乘坐游船，吹吹河风，歇歇脚，遥看整个古村落的全貌。伴随悠扬的音乐，坐在画舫之中，仿佛穿越回千年前的梦里水乡。'
        },
        {
            'src1': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp.jpg',
            'src2': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp%20(1).jpg',
            'name': '帝师客居宅',
            'intro': ' 陶瓷水镇紧邻甘陶河，风光秀美，人杰地灵，在甘陶河上有北方少见的画舫，乌篷船，和脚踏船，游完古村落，可以乘坐游船，吹吹河风，歇歇脚，遥看整个古村落的全貌。伴随悠扬的音乐，坐在画舫之中，仿佛穿越回千年前的梦里水乡。'
        }
    ]
    return render(request, 'vacation/food.html',context)

def commodity(request):
    context = {}
    context['title'] = '伴手礼'
    context['cont'] = [
        {
            'src1': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp.jpg',
            'src2': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp%20(1).jpg',
            'name': '帝师客居宅',
            'intro': ' 陶瓷水镇紧邻甘陶河，风光秀美，人杰地灵，在甘陶河上有北方少见的画舫，乌篷船，和脚踏船，游完古村落，可以乘坐游船，吹吹河风，歇歇脚，遥看整个古村落的全貌。伴随悠扬的音乐，坐在画舫之中，仿佛穿越回千年前的梦里水乡。'
        },
        {
            'src1': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp.jpg',
            'src2': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp%20(1).jpg',
            'name': '帝师客居宅',
            'intro': ' 陶瓷水镇紧邻甘陶河，风光秀美，人杰地灵，在甘陶河上有北方少见的画舫，乌篷船，和脚踏船，游完古村落，可以乘坐游船，吹吹河风，歇歇脚，遥看整个古村落的全貌。伴随悠扬的音乐，坐在画舫之中，仿佛穿越回千年前的梦里水乡。'
        },
        {
            'src1': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp.jpg',
            'src2': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp%20(1).jpg',
            'name': '帝师客居宅',
            'intro': ' 陶瓷水镇紧邻甘陶河，风光秀美，人杰地灵，在甘陶河上有北方少见的画舫，乌篷船，和脚踏船，游完古村落，可以乘坐游船，吹吹河风，歇歇脚，遥看整个古村落的全貌。伴随悠扬的音乐，坐在画舫之中，仿佛穿越回千年前的梦里水乡。'
        },
        {
            'src1': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp.jpg',
            'src2': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp%20(1).jpg',
            'name': '帝师客居宅',
            'intro': ' 陶瓷水镇紧邻甘陶河，风光秀美，人杰地灵，在甘陶河上有北方少见的画舫，乌篷船，和脚踏船，游完古村落，可以乘坐游船，吹吹河风，歇歇脚，遥看整个古村落的全貌。伴随悠扬的音乐，坐在画舫之中，仿佛穿越回千年前的梦里水乡。'
        }
    ]
    return render(request, 'vacation/commodity.html',context)

def play(request):
    context = {}
    context['title'] = '休闲娱乐'
    context['cont'] = [
        {
            'src1': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp.jpg',
            'src2': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp%20(1).jpg',
            'name': '帝师客居宅',
            'intro': ' 陶瓷水镇紧邻甘陶河，风光秀美，人杰地灵，在甘陶河上有北方少见的画舫，乌篷船，和脚踏船，游完古村落，可以乘坐游船，吹吹河风，歇歇脚，遥看整个古村落的全貌。伴随悠扬的音乐，坐在画舫之中，仿佛穿越回千年前的梦里水乡。'
        },
        {
            'src1': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp.jpg',
            'src2': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp%20(1).jpg',
            'name': '帝师客居宅',
            'intro': ' 陶瓷水镇紧邻甘陶河，风光秀美，人杰地灵，在甘陶河上有北方少见的画舫，乌篷船，和脚踏船，游完古村落，可以乘坐游船，吹吹河风，歇歇脚，遥看整个古村落的全貌。伴随悠扬的音乐，坐在画舫之中，仿佛穿越回千年前的梦里水乡。'
        },
        {
            'src1': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp.jpg',
            'src2': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp%20(1).jpg',
            'name': '帝师客居宅',
            'intro': ' 陶瓷水镇紧邻甘陶河，风光秀美，人杰地灵，在甘陶河上有北方少见的画舫，乌篷船，和脚踏船，游完古村落，可以乘坐游船，吹吹河风，歇歇脚，遥看整个古村落的全貌。伴随悠扬的音乐，坐在画舫之中，仿佛穿越回千年前的梦里水乡。'
        },
        {
            'src1': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp.jpg',
            'src2': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp%20(1).jpg',
            'name': '帝师客居宅',
            'intro': ' 陶瓷水镇紧邻甘陶河，风光秀美，人杰地灵，在甘陶河上有北方少见的画舫，乌篷船，和脚踏船，游完古村落，可以乘坐游船，吹吹河风，歇歇脚，遥看整个古村落的全貌。伴随悠扬的音乐，坐在画舫之中，仿佛穿越回千年前的梦里水乡。'
        }
    ]
    return render(request, 'vacation/play.html',context)
def service(request):
    context = {}
    context['title'] = '景区服务'
    return render(request, 'trip/service.html',context)