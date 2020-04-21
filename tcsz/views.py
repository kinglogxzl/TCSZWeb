from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def hello(request):  # request参数必须有，名字类似self的默认规则，可以修改，它封装了用户请求的所有内容
    # return HttpResponse("Hello world ! ")
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)


def index(request):
    context = {}
    meili = [
        {"name": '五彩灯笼', "path": '/static/img/水上项目/7.jpg', 'jj': '', 'xq': '详情'},
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
    # context['hello'] = 'Hello World!'
    return render(request, 'index.html', context)


def test(request):
    context = {}
    return render(request, 'traditional/summary.html', context)


def tradition(request):
    context = {}
    context['title'] = '水镇概述'
    return render(request, 'watertown/tradition.html', context)


def origin(request):
    context = {}
    context['title'] = '水镇渊源'
    return render(request, 'watertown/origin.html', context)


def celebrity(request):
    context = {}
    context['title'] = '水镇名人'
    return render(request, 'watertown/celebrity.html', context)


def custom(request):
    context = {}
    context['title'] = '水镇民俗'
    return render(request, 'watertown/custom.html', context)


def activity(request):
    context = {}
    context['title'] = '景区活动'
    return render(request, 'activity/activity.html', context)


def new(request):
    context = {}
    context['title'] = '新闻动态'
    return render(request, 'activity/new.html', context)


def notice(request):
    context = {}
    context['title'] = '景区公告'
    return render(request, 'activity/notice.html', context)
def traffic(request):
    context = {}
    context['title'] = '景区服务'
    return render(request, 'trip/traffic.html', context)
def strategy(request):
    context = {}
    context['title'] = '旅游攻略'
    return render(request, 'trip/strategy.html', context)
def video(request):
    context = {}
    context['title'] = '宣传影音'
    return render(request, 'video/video.html', context)



def accommodation(request):
    context = {}
    context['title'] = '住宿'
    context['cont'] = [
        {
            'src1': '/static/img/民宿/马家大院1.jpg',
            'src2': '/static/img/民宿/马家大院2.jpg',
            'name': '马家大院',
            'intro': ' 马家南院是个二进院子，三道门，前面还有一道屏风门，但很遗憾，这道古色的屏风在历史的过往中没了。'
        },
        {
            'src1': '/static/img/民宿/忠孝传家1.jpg',
            'src2': '/static/img/民宿/忠孝传家2.jpg',
            'name': '忠孝传家',
            'intro': '古朴悠长的孝经路,古色古香的家风馆，曲径通幽的村巷，清风徐来微波荡漾的甘陶河.'
        },
        {
            'src1': '/static/img/民宿/永春堂萱1.jpg',
            'src2': '/static/img/民宿/永春堂萱2.jpg',
            'name': '永春堂萱',
            'intro': '进入第一道大门是长方形空地一块，分南北中三个院落，布局合理、独特，是村内唯一一门三院建筑。大门上方门楣处悬挂“萱堂永春”祝寿匾额一块，蓝底金字，木字阴刻，是民国十年乡邻朋友祝寿赠送。该院落生活设施齐备，属宅俱全。'
        },
        {
            'src1': '/static/img/民宿/观陶水榭1.jpg',
            'src2': '/static/img/民宿/观陶水榭2.jpg',
            'name': '观陶水榭',
            'intro': '观陶水榭紧邻甘陶河，风光秀美，人杰地灵，在甘陶河上有北方少见的画舫，乌篷船，和脚踏船，游完古村落，可以乘坐游船，吹吹河风，歇歇脚，遥看整个古村落的全貌。伴随悠扬的音乐，坐在画舫之中，仿佛穿越回千年前的梦里水乡。'
        },
        {
            'src1': '/static/img/民宿/荷塘月色1.jpg',
            'src2': '/static/img/民宿/荷塘月色2.jpg',
            'name': '荷塘月色',
            'intro': '早上醒来，听雀鸣眉唱，放一段缠绵宛转的山西梆子，亦或听一曲古筝，人生之幸哪个能比? 绵绵细雨的午后，研磨执笔，胡乱涂写；再沏一壶香茶，真是听雨当琴，人生如斯。'
        },
        {
            'src1': '/static/img/民宿/陶岸憩斋1.jpg',
            'src2': '/static/img/民宿/陶岸憩斋2.jpg',
            'name': '陶岸憩斋',
            'intro': '那多情的水、那别致的院、那古老的瓷窑，构成一幅陶瓷水镇独具特色的江南水乡水墨画卷。'
        },
        {
            'src1': '/static/img/民宿/迓祉迎祥1.jpg',
            'src2': '/static/img/民宿/迓祉迎祥2.jpg',
            'name': '迓祉迎祥',
            'intro': '沿街望去，青砖黛瓦，斗拱垂檐，宛若回到了梦里故乡。大红灯笼高高挂，“陶瓷水镇南横口”。真的是未见秀水，已然见波。'
        },
        {
            'src1': '/static/img/民宿/双河别墅1.jpg',
            'src2': '/static/img/民宿/双河别墅2.jpg',
            'name': '双河别墅',
            'intro': ' 人生难得仙境处，陶瓷水镇在人间'
        }
    ]
    return render(request, 'vacation/accommodation.html', context)


def food(request):
    context = {}
    context['title'] = '美食'
    context['cont'] = [
        {
            'src1': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp.jpg',
            'src2': '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp%20(1).jpg',
            'name': '帝师客居宅测试',
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
    return render(request, 'vacation/food.html', context)


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
    return render(request, 'vacation/commodity.html', context)


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
    return render(request, 'vacation/play.html', context)


def service(request):
    context = {}
    context['title'] = '景区服务'
    return render(request, 'trip/service.html', context)
    return render(request, 'vacation/play.html', context)


def food_detail(request, name):
    context = {}
    context['title'] = name + '|陶瓷水镇'
    context['title2'] = '更多美食'
    food_list = {
        '帝师客居宅测试': [
            {"img": '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp.jpg',
             "p": ['陶瓷水镇紧邻甘陶河，风光秀美，人杰地灵，在甘陶河上有北方少见的画舫，乌篷船，和脚踏船，游完古村落，可以乘坐游船，吹吹河风，歇歇脚，遥看整个古村落的全貌。',
                   '伴随悠扬的音乐，坐在画舫之中，仿佛穿越回千年前的梦里水乡。']
             },
            {"img": '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp.jpg',
             "p": ['陶瓷水镇紧邻甘陶河，风光秀美，人杰地灵，在甘陶河上有北方少见的画舫，乌篷船，和脚踏船，游完古村落，可以乘坐游船，吹吹河风，歇歇脚，遥看整个古村落的全貌。',
                   '伴随悠扬的音乐，坐在画舫之中，仿佛穿越回千年前的梦里水乡。']
             }],
        '帝师客居宅': [
            {"img": '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp.jpg',
             "p": ['陶瓷水镇紧邻甘陶河，风光秀美，人杰地灵，在甘陶河上有北方少见的画舫，乌篷船，和脚踏船，游完古村落，可以乘坐游船，吹吹河风，歇歇脚，遥看整个古村落的全貌。',
                   '伴随悠扬的音乐，坐在画舫之中，仿佛穿越回千年前的梦里水乡。']
             },
            {"img": '/static/img/陶瓷水镇高端特色民宿图/帝师客居宅（四合院）/640.webp.jpg',
             "p": ['陶瓷水镇紧邻甘陶河，风光秀美，人杰地灵，在甘陶河上有北方少见的画舫，乌篷船，和脚踏船，游完古村落，可以乘坐游船，吹吹河风，歇歇脚，遥看整个古村落的全貌。',
                   '伴随悠扬的音乐，坐在画舫之中，仿佛穿越回千年前的梦里水乡。']
             }
        ]
    }
    more_data = []
    for item in food_list:
        if item != name:
            more_data.append({'name': item, 'img': food_list[item][0]['img']})
    context['data'] = food_list[name]
    context['idname'] = '美食'
    context['name'] = name
    context['more_data'] = more_data
    return render(request, 'vacation/detail.html', context)
