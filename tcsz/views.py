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
    context['cont'] = [
        {
            'src1': '/static/img/activity/01.jpg',
            'name': '借势旅发大会千年陶瓷之乡再绽芳华',
            'name1':'陶瓷水镇',
            'name2': '旅发大会',
            'name3': '井陉窑',
            'time': '2019.12.01',
            'intro': '井陉窑是历经隋、唐、宋、金、元、明、清等朝代的一处大型瓷窑址集群，距今已有千年历史。南横口村位于井陉县城南部,是历史古村，井陉现代陶瓷业的发源地，遗存县内规模最大、保存最为完整的古瓷密遗址。南横口古瓷窑是井陉窑的重要组成部分和典型代表。'
        },
        {
            'src1': '/static/img/activity/02.jpg',
            'name': '井陉古村落——陶瓷水镇新添红色文化主题展馆',
            'name1': '陶瓷水镇',
            'name2': '红色景区',
            'name3': '度假景区',
            'time': '2019.08.31',
            'intro': '景区精心打造的红色文化主题展馆举行了开展仪式，展馆展示的红色书籍、红色书画等千余件红色实物，吸引众多周围居民以及游客、学生等不同群体前来观展。'
        },
        {
            'src1': '/static/img/activity/03.jpg',
            'name': '陶瓷水镇新貌即将亮相石家庄第五届旅发大会！',
            'name1': '陶瓷水镇',
            'name2': '旅发大会',
            'name3': '古村落',
            'time': '2019.04.08',
            'intro': '本次旅发大会以“太行风情古陉新韵”为主题，以“活旅游、聚产业、促发展、惠民生”为宗旨，依托井陉千年古县、百年老矿文化底蕴和生态资源优势，实施旅游公共服务设施提升工程、景区设施提档和新项目建设工程，丰富当地旅游资源，打造传统古村落片区。'
        }
    ]
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
            'intro': '马家大院位于村子的正中央，是清代轶士马席珍的故居，历经一百多年的历史沧桑，仍旧矗立在这个古老的村庄。整个院落古典而错落有致，华丽而不奢靡，在瓦片和屋檐下，烛光闪闪，想必有很多值得探索的故事！院内有三间民宿，分别为素雅、淳朴、勤勉，每间客房面积均为20㎡左右，每间客房内都带有独立卫生间。山景之中的日出，河韵之中的秀石，美景与远方，时光与情怀，享受与自在。'
        },
        {
            'src1': '/static/img/民宿/忠孝传家1.jpg',
            'src2': '/static/img/民宿/忠孝传家2.jpg',
            'name': '忠孝传家',
            'intro': '忠孝传家远，诗书继世长。忠孝传家院落是中式装修风格，院内共有三间民宿，院内配有厨房，三五好友，住在这样的院落，好不惬意。院内面积30㎡左右，院内三间民宿分别为睿智、礼仪、仁慈义德，每间客房面积均在25㎡左右，配有公共卫生间。'
        },
        {
            'src1': '/static/img/民宿/永春堂萱1.jpg',
            'src2': '/static/img/民宿/永春堂萱2.jpg',
            'name': '永春堂萱',
            'intro': '永春堂萱（一宅三院）民宿院内20㎡左右，院内有三间民宿，分别为清闲、安逸、甜淡，每间客房面积均为15㎡左右，三间客房公用卫生间。民宿，让赶路者放缓了脚步，在慢时光下懂得慢享受；让旅行者为之倾倒，寻觅宁静中的那份洒脱；让寻梦者为之惊叹，如诗梦一样的经营生活。有形、有意、有境，民宿之美，美在年代感；民宿之美，美在有灵魂。'
        },
        {
            'src1': '/static/img/民宿/观陶水榭1.jpg',
            'src2': '/static/img/民宿/观陶水榭2.jpg',
            'name': '观陶水榭',
            'intro': '观陶水榭民宿院位于一宅三院民宿院旁，民宿院内分为上下两层，装修都为中式风格，院内面积30㎡左右，院内有三间民宿房，分别为悟禅、静夜思、听风赏月，悟禅房间面积稍小，15㎡左右，静夜思和听风赏月面积均为30㎡左右，每间客房内都带有独立卫生间。迷人的民宿，好似一家富有情怀的小酒馆，里面藏着各种美味的酒。休憩之日，与三五老友小聚一餐，醉人的佳酿入口，思绪慢慢的走，带你回到美好的年代'
        },
        {
            'src1': '/static/img/民宿/荷塘月色1.jpg',
            'src2': '/static/img/民宿/荷塘月色2.jpg',
            'name': '荷塘月色',
            'intro': '荷塘月色民宿院临近甘陶河，推开房门映入眼帘的是甘陶河的风景，山和游船相呼应，在夜晚更深切的体会到古村落的寂静。荷塘月色院内装修均为榻榻米风格，院内面积25㎡左右，院内有四间民宿房，分别为长思、采莲、静坐、益养天年，每间客房面积均为25㎡左右，每间客房内都带有独立卫生间。纯净的天空，梦幻的远方，繁华之外，安静之上，或栖于村寨，享受原始与淳朴。'
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
            'src1': '/static/img/美食/ji.jpg',
            'src2': '/static/img/美食/1.jpg',
            'name': '村里那只鸡',
            'intro': ' 煮着鸡汤的铁锅边再围上一圈的玉米面饼子，盖上锅盖，铁锅中的蒸汽连同锅壁的温度一起将饼焖熟。焖好的饼松软可口，再配上一碗鲜美的鸡汤，这味道绝了！'
        },
        {
            'src1': '/static/img/美食/df.jpg',
            'src2': '/static/img/美食/1.jpg',
            'name': '水镇黑豆腐',
            'intro': ' 黑豆腐的制作是个手艺活，也是醉淳朴的坚守，当地的好山泉，制作不加石膏，全靠大石板压制出扎实而沉甸甸的豆腐，带着自然粗糙的气孔。除了糙实和灰色的外表，其实最让人会沉迷的，还是一股裹着豆香的炭火焦香，这气味会让人想起农村的大锅里烧出的饭菜香，不少人会在闻到这股独特豆香的时候被感动到。'
        },
        {
            'src1': '/static/img/美食/dgc.jpg',
            'src2': '/static/img/美食/1.jpg',
            'name': '大锅菜',
            'intro': ' 大锅菜又名熬菜，是一道色香味俱全的传统名菜，中国北方地区常见菜品之一，在北方地区较流行。食材多样，营养丰富，汤汁浓郁。此菜其名称的由来，首先是它有很多种菜的风味，其次就是说在早年大家是在一起吃饭一起干活，所以就叫做了大锅菜。'
        },
        {
            'src1': '/static/img/美食/yu.jpg',
            'src2': '/static/img/美食/1.jpg',
            'name': '鱼和豆腐的故事',
            'intro': ' 鱼和豆腐本是绝配，这道鳗鱼肉馅酿豆腐，既有鱼的鲜美，也有肉的丰腴，更有豆腐的清香，一口下去，回味无穷~'
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
            'src1': '/static/img/娱乐/hq.jpg',
            'src2': '/static/img/娱乐/hq1.jpg',
            'name': '呐喊喷泉',
            'intro': ' 网红呐喊喷泉不仅能“闻”声起舞，还能伴随呐喊声持续上升，声音越持久喷泉越高。如果你的肺活量爆棚的话，你将会看到这道水光与蓝天白云举案齐眉的壮观景象，惊叹它的神奇！在这样一个天然氧吧里放声呐喊，释放激情！释放压力!'
        },
        {
            'src1': '/static/img/娱乐/hf.jpg',
            'src2': '/static/img/娱乐/hf1.jpg',
            'name': '画舫',
            'intro': ' 艳唱潮初落，江花露未晞。春洲惊翡翠，朱服弄芳菲。画舫烟中浅，青阳日际微。锦帆冲浪湿，罗袖拂行衣。含情罢所采，相叹惜流晖。'
        },
        {
            'src1': '/static/img/娱乐/jtc.jpg',
            'src2': '/static/img/娱乐/jtc1.jpg',
            'name': '脚踏船',
            'intro': '集运动、娱乐、休闲等功能于一体，满足个人及家庭享受生活的需要。在发展中国家，脚踏船多作为公园、旅游景点的经营项目供人们消费，少量也作为个人的游玩手段。'
        },
        {
            'src1': '/static/img/娱乐/wpc.jpg',
            'src2': '/static/img/娱乐/wpc1.jpg',
            'name': '乌篷船',
            'intro': ' 碧波漫透的水，乌篷船飘于上面，不禁令人想到无数的描写江南水乡的诗句，想到那诗情画意的地方。碧绿的水面浮着一叶叶小船，飘飘摇摇，载的是一种闲适，一份雅情。'
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
        '村里那只鸡': [
            {"img": '/static/img/美食/ji.jpg',
             "p": ['煮着鸡汤的铁锅边再围上一圈的玉米面饼子，盖上锅盖，铁锅中的蒸汽连同锅壁的温度一起将饼焖熟。']
             },
            {"img": '/static/img/美食/1.jpg',
             "p": ['焖好的饼松软可口，再配上一碗鲜美的鸡汤，这味道绝了！']
             }],
        '水镇黑豆腐': [
            {"img": '/static/img/美食/df.jpg',
             "p": ['黑豆腐的制作是个手艺活，也是醉淳朴的坚守，当地的好山泉，制作不加石膏，全靠大石板压制出扎实而沉甸甸的豆腐，带着自然粗糙的气孔。']
             },
            {"img": '/static/img/美食/1.jpg',
             "p": ['除了糙实和灰色的外表，其实最让人会沉迷的，还是一股裹着豆香的炭火焦香，这气味会让人想起农村的大锅里烧出的饭菜香，不少人会在闻到这股独特豆香的时候被感动到。']
             }
        ],
        '大锅菜': [
            {"img": '/static/img/美食/dgc.jpg',
             "p": ['大锅菜又名熬菜，是一道色香味俱全的传统名菜，中国北方地区常见菜品之一，在北方地区较流行。食材多样，营养丰富，汤汁浓郁。']
             },
            {"img": '/static/img/美食/1.jpg',
             "p": ['此菜其名称的由来，首先是它有很多种菜的风味，其次就是说在早年大家是在一起吃饭一起干活，所以就叫做了大锅菜。']
             }
        ],
        '鱼和豆腐的故事': [
            {"img": '/static/img/美食/yu.jpg',
             "p": ['鱼和豆腐本是绝配，这道鳗鱼肉馅酿豆腐，既有鱼的鲜美，也有肉的丰腴，更有豆腐的清香，一口下去，回味无穷']
             },
            {"img": '/static/img/美食/1.jpg',
             "p": ['']
             }
        ]
    }
    more_data = []
    for item in food_list:
        if item != name:
            more_data.append({'name': item, 'img': food_list[item][0]['img']})
    context['data'] = food_list[name]
    context['idname'] = '美食'
    context['tname'] = 'food'
    context['name'] = name
    context['more_data'] = more_data
    return render(request, 'vacation/detail.html', context)

def accommodation_detail(request, name):
    context = {}
    context['title'] = name + '|陶瓷水镇'
    context['title2'] = '更多房间'
    accommodation_list = {
        '马家大院': [
            {"img": '/static/img/民宿/马家大院1.jpg',
             "p": ['马家大院位于村子的正中央，是清代轶士马席珍的故居，历经一百多年的历史沧桑，仍旧矗立在这个古老的村庄。']
             },
            {"img": '/static/img/民宿/马家大院2.jpg',
             "p": ['整个院落古典而错落有致，华丽而不奢靡，在瓦片和屋檐下，烛光闪闪，想必有很多值得探索的故事！院内有三间民宿，分别为素雅、淳朴、勤勉，每间客房面积均为20㎡左右，每间客房内都带有独立卫生间。山景之中的日出，河韵之中的秀石，美景与远方，时光与情怀，享受与自在。']
             }],
        '忠孝传家': [
            {"img": '/static/img/民宿/忠孝传家1.jpg',
             "p": ['忠孝传家远，诗书继世长。忠孝传家院落是中式装修风格，院内共有三间民宿，院内配有厨房，三五好友，住在这样的院落，好不惬意。']
             },
            {"img": '/static/img/民宿/忠孝传家2.jpg',
             "p": ['院内面积30㎡左右，院内三间民宿分别为睿智、礼仪、仁慈义德，每间客房面积均在25㎡左右，配有公共卫生间。']
             }
        ],
        '永春堂萱': [
            {"img": '/static/img/民宿/永春堂萱1.jpg',
             "p": ['永春堂萱（一宅三院）民宿院内20㎡左右，院内有三间民宿，分别为清闲、安逸、甜淡，每间客房面积均为15㎡左右，三间客房公用卫生间。民宿，让赶路者放缓了脚步，在慢时光下懂得慢享受；']
             },
            {"img": '/static/img/民宿/永春堂萱2.jpg',
             "p": ['让旅行者为之倾倒，寻觅宁静中的那份洒脱；让寻梦者为之惊叹，如诗梦一样的经营生活。有形、有意、有境，民宿之美，美在年代感；民宿之美，美在有灵魂。']
             }
        ],
        '观陶水榭': [
            {"img": '/static/img/民宿/观陶水榭1.jpg',
             "p": ['观陶水榭民宿院位于一宅三院民宿院旁，民宿院内分为上下两层，装修都为中式风格，院内面积30㎡左右，院内有三间民宿房，分别为悟禅、静夜思、听风赏月，悟禅房间面积稍小，15㎡左右，静夜思和听风赏月面积均为30㎡左右，每间客房内都带有独立卫生间。']
             },
            {"img": '/static/img/民宿/观陶水榭2.jpg',
             "p": ['迷人的民宿，好似一家富有情怀的小酒馆，里面藏着各种美味的酒。休憩之日，与三五老友小聚一餐，醉人的佳酿入口，思绪慢慢的走，带你回到美好的年代']
             }
        ],
        '荷塘月色': [
            {"img": '/static/img/民宿/荷塘月色1.jpg',
             "p": [
                 '荷塘月色民宿院临近甘陶河，推开房门映入眼帘的是甘陶河的风景，山和游船相呼应，在夜晚更深切的体会到古村落的寂静。']
             },
            {"img": '/static/img/民宿/荷塘月色2.jpg',
             "p": ['荷塘月色院内装修均为榻榻米风格，院内面积25㎡左右，院内有四间民宿房，分别为长思、采莲、静坐、益养天年，每间客房面积均为25㎡左右，每间客房内都带有独立卫生间。纯净的天空，梦幻的远方，繁华之外，安静之上，或栖于村寨，享受原始与淳朴']
             }
        ],
        '陶岸憩斋': [
            {"img": '/static/img/民宿/陶岸憩斋1.jpg',
             "p": [
                 '陶岸憩斋是离景区中心较远的一处民宿院落。因所有的墙体建筑以及地面都使用烧瓷时用的耐火砖，而耐火砖的砖体表面颜色呈金黄色，故名为“黄金屋”。']
             },
            {"img": '/static/img/民宿/陶岸憩斋2.jpg',
             "p": ['院内面积40㎡左右，院内有四间民宿，分别为松、竹、美、兰，每间客房面积均为20㎡左右，每间客房内都带有独立卫生间。民宿或许是寻觅归属感的最佳地方，在这里可以让你摆脱都市压力的束缚，让疲惫的心灵得到宝贵的歇息机会，更重要的是可以找寻到久违的归属感，遇见最美的自己。']
             }
        ],
        '迓祉迎祥': [
            {"img": '/static/img/民宿/迓祉迎祥1.jpg',
             "p": [
                 '“迓，迎也。古本皆作讶。祉，福也，禄也。迎祥 ，迎纳吉祥。”']
             },
            {"img": '/static/img/民宿/迓祉迎祥2.jpg',
             "p": [
                 '迓祉迎祥院内面积20㎡左右，院内有三间民宿，分别为福瑞、祥和、厚德载物，每间客房面积均为17㎡左右，每间客房内都带有独立卫生间。行在胡同里，住在人情里。陶瓷水镇民宿，你来，春暖花开。']
             }
        ],
        '双河别墅': [
            {"img": '/static/img/民宿/双河别墅1.jpg',
             "p": [
                 '人生难得仙境处，陶瓷水镇在人间']
             },
            {"img": '/static/img/民宿/双河别墅2.jpg',
             "p": [
                 '沿街望去，青砖黛瓦，斗拱垂檐，宛若回到了梦里故乡。大红灯笼高高挂，“陶瓷水镇南横口”。真的是未见秀水，已然见波。']
             }
        ]
    }
    more_data = []
    for item in accommodation_list:
        if item != name:
            more_data.append({'name': item, 'img': accommodation_list[item][0]['img']})
    context['data'] = accommodation_list[name]
    context['idname'] = '住宿'
    context['tname'] = 'accommodation'
    context['name'] = name
    context['more_data'] = more_data
    return render(request, 'vacation/detail.html', context)


def play_detail(request, name):
    context = {}
    context['title'] = name + '|陶瓷水镇'
    context['title2'] = '更多娱乐项目'
    play_list = {
        '呐喊喷泉': [
            {"img": '/static/img/娱乐/hq.jpg',
             "p": ['网红呐喊喷泉不仅能“闻”声起舞，还能伴随呐喊声持续上升，声音越持久喷泉越高。']
             },
            {"img": '/static/img/娱乐/hq1.jpg',
             "p": ['如果你的肺活量爆棚的话，你将会看到这道水光与蓝天白云举案齐眉的壮观景象，惊叹它的神奇！在这样一个天然氧吧里放声呐喊，释放激情！释放压力!']
             }],
        '画舫': [
            {"img": '/static/img/娱乐/hf.jpg',
             "p": ['艳唱潮初落，江花露未晞。春洲惊翡翠，朱服弄芳菲。']
             },
            {"img": '/static/img/娱乐/hf1.jpg',
             "p": ['画舫烟中浅，青阳日际微。锦帆冲浪湿，罗袖拂行衣。含情罢所采，相叹惜流晖。']
             }
        ],
        '脚踏船': [
            {"img": '/static/img/娱乐/jtc.jpg',
             "p": ['集运动、娱乐、休闲等功能于一体，满足个人及家庭享受生活的需要。']
             },
            {"img": '/static/img/娱乐/jtc1.jpg',
             "p": ['在发展中国家，脚踏船多作为公园、旅游景点的经营项目供人们消费，少量也作为个人的游玩手段。']
             }
        ],
        '乌篷船': [
            {"img": '/static/img/娱乐/wpc.jpg',
             "p": ['碧波漫透的水，乌篷船飘于上面，不禁令人想到无数的描写江南水乡的诗句，想到那诗情画意的地方。']
             },
            {"img": '/static/img/娱乐/wpc1.jpg',
             "p": ['碧绿的水面浮着一叶叶小船，飘飘摇摇，载的是一种闲适，一份雅情。']
             }
        ]
    }
    more_data = []
    for item in play_list:
        if item != name:
            more_data.append({'name': item, 'img': play_list[item][0]['img']})
    context['data'] = play_list[name]
    context['idname'] = '休闲娱乐'
    context['tname'] = 'play'
    context['name'] = name
    context['more_data'] = more_data
    return render(request, 'vacation/detail.html', context)


def new_detail(request, name):
    context = {}
    context['title'] = name + '|陶瓷水镇'
    context['title2'] = '更多新闻动态'
    new_list = {
        '借势旅发大会千年陶瓷之乡再绽芳华': [
            {"img": '/static/img/activity/lf1.jpg',
             "p": ['井陉窑是历经隋、唐、宋、金、元、明、清等朝代的一处大型瓷窑址集群，距今已有千年历史。南横口村位于井陉县城南部,是历史古村，井陉现代陶瓷业的发源地，遗存县内规模最大、保存最为完整的古瓷密遗址。南横口古瓷窑是井陉窑的重要组成部分和典型代表。作为石家庄市第五届旅发大会重要景点之一的陶瓷水镇，就是依托南横口村古瓷窑遗址片区重新规划而建。']
             },
            {"img": '/static/img/activity/lf2.jpg',
             "p": ['一进入陶瓷水镇，仿若置身于花海中的江南小镇，各种厨房里常见的砂锅、瓷碗、水瓮、菜坛等都被排列成各种造型，镶嵌在景区的景观墙上，古朴中透着雅致，古时人的厨房“旧爱”摇身一变成为了现代人的“新欢”，这些盆盆罐罐的装饰如此的别具一格，每一个新颖的造型都让人眼前一亮。陶瓷水镇把匣钵(笼盔)、陶砖植入古民居独有特点,赋予了南横口古民居独有的笼盔文化、红石文化和窑砖文化特征，置身其间,我们仿佛游润于一座露天瓷艺建筑博物馆。']
             }],
        '井陉古村落——陶瓷水镇新添红色文化主题展馆': [
            {"img": '/static/img/activity/hs2.jpg',
             "p": ['陶瓷水镇位于井陉县南横口村，是井陉县重点打造的一处集观光游览、休闲度假、创意文化、滨水娱乐等旅游业态为一体的山水休闲旅游度假景区。12月26日上午，景区精心打造的红色文化主题展馆举行了开展仪式，展馆展示的红色书籍、红色书画等千余件红色实物，吸引众多周围居民以及游客、学生等不同群体前来观展。']
             },
            {"img": '/static/img/activity/hs1.jpg',
             "p": ['，同时也有效提升了陶瓷水镇的旅游文化产业发展，吸引了人气，让市民到陶瓷水镇旅游观光的同时，感受红色历史文化，激发大家干事创业的红色能量，引导人们特别是广大青少年切实增强历史使命感和责任感，更加珍惜现在的美好生活。']
             }
        ],
        '陶瓷水镇新貌即将亮相石家庄第五届旅发大会！': [
            {"img": '/static/img/activity/lf3.jpg',
             "p": ['作为石家庄市第五届旅发大会重要景点之一，按照旅发大会筹委会的总体规划设计，目前，南横口村陶瓷水镇景区各景点准备工作基本就绪，个别节点正在进一步精细化打造中。走进井陉县秀水镇南横口村陶瓷水镇，可以感受到这里的陶瓷文化。镶嵌在景观墙上的别致陶瓷造型、整齐排列的新颖盆罐、特制的巨型白瓷瓶景观......']
             },
            {"img": '/static/img/activity/lf4.jpg',
             "p": ['次旅发大会以“太行风情 古陉新韵”为主题，以“活旅游、聚产业、促发展、惠民生”为宗旨，依托井陉千年古县、百年老矿文化底蕴和生态资源优势，实施旅游公共服务设施提升工程、景区设施提档和新项目建设工程，丰富当地旅游资源，打造传统古村落片区。另外，大会期间，井陉拉花、花脸社火、苍岩龙鼓、秦皇古乐、锣架鼓、丝弦、竹马等国家级省级非遗节目将悉数亮相。']
             }
        ]
    }
    more_data = []
    for item in new_list:
        if item != name:
            more_data.append({'name': item, 'img': new_list[item][0]['img']})
    context['data'] = new_list[name]
    context['idname'] = '新闻动态'
    context['tname'] = 'new'
    context['name'] = name
    context['more_data'] = more_data
    return render(request, 'activity/detail.html', context)