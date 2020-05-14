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
        {"name": '五彩灯笼', "path": 'http://image.taocishuizhen.com/水上项目/7.jpg', 'jj': '', 'xq': '详情'},
        {"name": '庭院一角', "path": 'http://image.taocishuizhen.com/水上项目/2.jpg', 'jj': '', 'xq': '详情'},
        {"name": '古镇门楼', "path": 'http://image.taocishuizhen.com/水上项目/11.jpg', 'jj': '', 'xq': '详情'},
        {"name": '水镇夜景', "path": 'http://image.taocishuizhen.com/水上项目/3.jpg', 'jj': '', 'xq': '详情'},
        {"name": '水镇夜景', "path": 'http://image.taocishuizhen.com/水上项目/10.jpg', 'jj': '', 'xq': '详情'},
        {"name": '水上项目', "path": 'http://image.taocishuizhen.com/水上项目/9.jpg', 'jj': '', 'xq': '详情'},
        {"name": '水边民宿', "path": 'http://image.taocishuizhen.com/水上项目/1.jpg', 'jj': '', 'xq': '详情'},
        {"name": '水上古船', "path": 'http://image.taocishuizhen.com/水上项目/8.jpg', 'jj': '', 'xq': '详情'},
        {"name": '石太铁路', "path": 'http://image.taocishuizhen.com/水上项目/6.jpg', 'jj': '', 'xq': '详情'},
        {"name": '景区远景', "path": 'http://image.taocishuizhen.com/水上项目/5.jpg', 'jj': '', 'xq': '详情'},
        {"name": '景区俯景', "path": 'http://image.taocishuizhen.com/水上项目/4.jpg', 'jj': '', 'xq': '详情'},
        {"name": '河中小岛', "path": 'http://image.taocishuizhen.com/水上项目/12.jpg', 'jj': '', 'xq': '详情'}
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
    context['cont'] = [
        {
            'src1': 'http://image.taocishuizhen.com/activity/1.jpg',
            'name': '“迎国庆”井陉陶瓷水镇民俗文化节启动仪式',
            'name1': '民俗文化节',
            'name2': '井陉陶瓷',
            'name3': '陶瓷水镇',
            'time': '2019.12.01',
            'intro': ' 千呼万唤的“迎国庆”井陉陶瓷水镇首届民俗文化节，盛邀全国具有版权的节庆团队，携手各路网红美食家，超100+星厨美味，为您而来！ '
        },
        {
            'src1': 'http://image.taocishuizhen.com/activity/2.jpg',
            'name': '陶瓷水镇-社火表演',
            'name1': '陶瓷水镇',
            'name2': '井陉社火',
            'name3': '非物质文化遗产',
            'time': '2020.5.4',
            'intro': '  5月4日上午陶瓷水镇迎来了国家非物质文化遗产"社火"的演出。 '
        },
        {
            'src1': 'http://image.taocishuizhen.com/activity/03.jpg',
            'name': '陶瓷水镇新貌即将亮相石家庄第五届旅发大会',
            'name1': '陶瓷水镇',
            'name2': '旅发大会',
            'name3': '石家庄井陉',
            'time': '2019.08.08',
            'intro': '  作为石家庄市第五届旅发大会重要景点之一，按照旅发大会筹委会的总体规划设计，目前，南横口村陶瓷水镇景区各景点准备工作基本就绪，个别节点正在进一步精细化打造中。 '
        },
        {
            'src1': 'http://image.taocishuizhen.com/activity/02.jpg',
            'name': '陶瓷水镇红色文化主题展馆举行开展仪式',
            'name1': '陶瓷水镇',
            'name2': '主题展馆',
            'name3': '红色文化',
            'time': '2020.01.08',
            'intro': '陶瓷水镇红色文化主题展馆举行开展仪式。 '
        },
        {
            'src1': 'http://image.taocishuizhen.com/activity/4.jpg',
            'name': '曾经杭州西湖断桥爱情美，如今河北陶瓷水镇迎恋情',
            'name1': '陶瓷水镇',
            'name2': '相亲会',
            'name3': '遇见爱情',
            'time': '2020.02.08',
            'intro': '爱情就是一次旅途，要去的地方名字叫做“幸福”。遇见谁都是一个美丽的意外，将压力与不良心绪格式化，释放快乐因子，抚慰躁动的心，携手闯关，画舫中汉服美女巧笑嫣然与岸边男子互动，体验制作陶瓷工艺，共同见证爱情初体验。 '
        },
        ]
    return render(request, 'activity/activity.html', context)


def new(request):
    context = {}
    context['title'] = '新闻动态'
    context['cont'] = [
        {
            'src1': 'http://image.taocishuizhen.com/activity/01.jpg',
            'name': '借势旅发大会千年陶瓷之乡再绽芳华',
            'name1':'陶瓷水镇',
            'name2': '旅发大会',
            'name3': '井陉窑',
            'time': '2019.12.01',
            'intro': '井陉窑是历经隋、唐、宋、金、元、明、清等朝代的一处大型瓷窑址集群，距今已有千年历史。南横口村位于井陉县城南部,是历史古村，井陉现代陶瓷业的发源地，遗存县内规模最大、保存最为完整的古瓷密遗址。南横口古瓷窑是井陉窑的重要组成部分和典型代表。'
        },
        {
            'src1': 'http://image.taocishuizhen.com/activity/02.jpg',
            'name': '井陉古村落——陶瓷水镇新添红色文化主题展馆',
            'name1': '陶瓷水镇',
            'name2': '红色景区',
            'name3': '度假景区',
            'time': '2019.08.31',
            'intro': '景区精心打造的红色文化主题展馆举行了开展仪式，展馆展示的红色书籍、红色书画等千余件红色实物，吸引众多周围居民以及游客、学生等不同群体前来观展。'
        },
        {
            'src1': 'http://image.taocishuizhen.com/activity/03.jpg',
            'name': '陶瓷水镇新貌即将亮相石家庄第五届旅发大会！',
            'name1': '陶瓷水镇',
            'name2': '旅发大会',
            'name3': '古村落',
            'time': '2019.04.08',
            'intro': '本次旅发大会以“太行风情古陉新韵”为主题，以“活旅游、聚产业、促发展、惠民生”为宗旨，依托井陉千年古县、百年老矿文化底蕴和生态资源优势，实施旅游公共服务设施提升工程、景区设施提档和新项目建设工程，丰富当地旅游资源，打造传统古村落片区。'
        },
        {
            'src1': 'http://image.taocishuizhen.com/activity/1.jpg',
            'name': '井陉陶瓷水镇民俗文化节启动',
            'name1': '陶瓷水镇',
            'name2': '民俗文化节',
            'name3': '井陉',
            'time': '2019.09.08',
            'intro': '千年瓷韵展芳华，魅力水乡似江南。9月28日上午，由井陉县委宣传部主办，河北华秀文化旅游有限公司承办的“‘迎国庆’井陉陶瓷水镇民俗文化节”在位于井陉县秀林镇的“南横口陶瓷水镇”正式启动。'
        }
    ]
    return render(request, 'activity/new.html', context)

def notice(request):
    context = {}
    context['title'] = '景区公告'
    context['cont'] = [
        {
            'name': '井陉：陶瓷水镇南横口喜迎第四届省旅发大会观摩团',
            'time1': '2020',
            'time2': '10.16',
            'intro': '10月16日上午旅发观摩团分两批来到井陉县陶瓷水镇南横口进行观摩...'
        },
        {
            'name': '文旅部、国家卫健委联合下发《通知》 严格规范景区管理',
            'time1': '2020',
            'time2': '4.13',
            'intro': '4月13日，经国务院应对新型冠状病毒感染肺炎疫情联防联控机制同意，文化和旅游部、国家卫生健康委联合印发《关于做好旅游景区疫情防控和安全有序开放工作的通知》...'
        },
        {
            'name': '旅游景区接待游客量不得超过核定最大承载量的30%...',
            'time1': '2020',
            'time2': '4.23',
            'intro': '根据《通知》，景区需坚持防控为先，实行限量开放。各地在做好旅游景区疫情防控工作的前提下，坚持分区分级原则，严格落实《旅游景区恢复开放疫情防控措施指南》要求，做到限量、有序开放，严防无序开放。...'
        },
        {
            'name': '关于进一步加强公共场所新冠肺炎疫情防控工作的通告...',
            'time1': '2020',
            'time2': '4.15',
            'intro': '为进一步加强公共场所疫情防控，严防疫情反弹，根据省、市疫情防控相关工作要求，现就有关要求通知如下...'
        },
        {
            'name': '关于应对新冠肺炎疫情影响加快服务业发展的工作方案...',
            'time1': '2020',
            'time2': '4.19',
            'intro': '根据疫情防控形势和服务业行业发展特点，结合2020年我市经济工作总体部署，应对疫情影响，实现“以丰补歉”，加快服务业高质量发展工作分三个阶段推进...'
        },
        {
            'name': '复工复产后，企业、景区等公共场所的防疫措施如何做？...',
            'time1': '2020',
            'time2': '4.23',
            'intro': '关于旅游景区，中国疾控中心一方面强调恢复开业前一系列的准备工作，特别是一些物资的准备，包括采购足够的口罩、消毒剂、洗手液、速干手消毒剂以及体温计等等这些防护物资。...'
        }
    ]
    return render(request, 'activity/notice.html', context)
def traffic(request):
    context = {}
    context['title'] = '景区服务'
    return render(request, 'trip/traffic.html', context)
def strategy(request):
    context = {}
    context['title'] = '旅游攻略'
    context['cont'] = [
        {
        'name': '陶瓷水镇——带上好心情出发吧！！！',
        'time': '2020-01-06',
        'src': 'http://image.taocishuizhen.com/trip/youji1.jpg',
        'intro': '古风古色，陶瓷砖瓦搭建的墙壁，也不知道多少是新修，多少是原本的面貌了，但是走在窄窄的巷子里，高高低低的陡峭，还是体会的到曾经古老的生活。'
        },

        {
            'name': '石家庄周边游古村落篇—南横口陶瓷水镇',
            'time': '2020-03-06',
            'src': 'http://image.taocishuizhen.com/trip/youji2.jpg',
            'intro': '从去年的旅发大会我就听说井陉有个陶瓷水镇，今天终于有机会来陶瓷水镇啦... ...'
        },
        {
            'name': '井陉有个南横口，凭水临风。',
            'time': '2020-04-06',
            'src': 'http://image.taocishuizhen.com/trip/youji3.jpg',
            'intro': '空气很好，水很干净，古香古色，疫情期间，人也并不是很多。看景，玩水，赏花，人文，都是不错的选择。'
        },
        {
            'name': '周末野游',
            'time': '2020-03-06',
            'src': 'http://image.taocishuizhen.com/trip/youji4.jpg',
            'intro': '开到周末了，给大家推荐一个游玩好去处，井陉陶瓷水镇，古朴风格，水镇很纯朴，原来的一个民窑，以各式陶瓷装饰为主的风格，适合一家人轻松游玩'
        },
        {
            'name': '有山有水的好地方',
            'time': '2020-02-06',
            'src': 'http://image.taocishuizhen.com/trip/youji5.jpg',
            'intro': '有山有水的地方一直是我心中向往的，美景怡人，特殊时期，人不是很多，对于喜静的人来说刚刚好，现在正是最适合来这里的季节！'
        },
        {
            'name': '陶瓷水镇游记',
            'time': '2020-04-08',
            'src': 'http://image.taocishuizhen.com/trip/youji6.jpg',
            'intro': '邢窑、定窑、磁州窑、井陉窑被称为河北四大名窑，在中国瓷器文化的历史长河中为河北留下了灿烂身影。而井陉窑最具代表性的就是南横口。'
        }
    ]
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
            'src1': 'http://image.taocishuizhen.com/民宿/马家大院1.jpg',
            'src2': 'http://image.taocishuizhen.com/民宿/马家大院2.jpg',
            'name': '马家大院',
            'intro': '马家大院位于村子的正中央，是清代轶士马席珍的故居，历经一百多年的历史沧桑，仍旧矗立在这个古老的村庄。整个院落古典而错落有致，华丽而不奢靡，在瓦片和屋檐下，烛光闪闪，想必有很多值得探索的故事！院内有三间民宿，分别为素雅、淳朴、勤勉，每间客房面积均为20㎡左右，每间客房内都带有独立卫生间。山景之中的日出，河韵之中的秀石，美景与远方，时光与情怀，享受与自在。'
        },
        {
            'src1': 'http://image.taocishuizhen.com/民宿/忠孝传家1.jpg',
            'src2': 'http://image.taocishuizhen.com/民宿/忠孝传家2.jpg',
            'name': '忠孝传家',
            'intro': '忠孝传家远，诗书继世长。忠孝传家院落是中式装修风格，院内共有三间民宿，院内配有厨房，三五好友，住在这样的院落，好不惬意。院内面积30㎡左右，院内三间民宿分别为睿智、礼仪、仁慈义德，每间客房面积均在25㎡左右，配有公共卫生间。'
        },
        {
            'src1': 'http://image.taocishuizhen.com/民宿/永春堂萱1.jpg',
            'src2': 'http://image.taocishuizhen.com/民宿/永春堂萱2.jpg',
            'name': '永春堂萱',
            'intro': '永春堂萱（一宅三院）民宿院内20㎡左右，院内有三间民宿，分别为清闲、安逸、甜淡，每间客房面积均为15㎡左右，三间客房公用卫生间。民宿，让赶路者放缓了脚步，在慢时光下懂得慢享受；让旅行者为之倾倒，寻觅宁静中的那份洒脱；让寻梦者为之惊叹，如诗梦一样的经营生活。有形、有意、有境，民宿之美，美在年代感；民宿之美，美在有灵魂。'
        },
        {
            'src1': 'http://image.taocishuizhen.com/民宿/观陶水榭1.jpg',
            'src2': 'http://image.taocishuizhen.com/民宿/观陶水榭2.jpg',
            'name': '观陶水榭',
            'intro': '观陶水榭民宿院位于一宅三院民宿院旁，民宿院内分为上下两层，装修都为中式风格，院内面积30㎡左右，院内有三间民宿房，分别为悟禅、静夜思、听风赏月，悟禅房间面积稍小，15㎡左右，静夜思和听风赏月面积均为30㎡左右，每间客房内都带有独立卫生间。迷人的民宿，好似一家富有情怀的小酒馆，里面藏着各种美味的酒。休憩之日，与三五老友小聚一餐，醉人的佳酿入口，思绪慢慢的走，带你回到美好的年代'
        },
        {
            'src1': 'http://image.taocishuizhen.com/民宿/荷塘月色1.jpg',
            'src2': 'http://image.taocishuizhen.com/民宿/荷塘月色2.jpg',
            'name': '荷塘月色',
            'intro': '荷塘月色民宿院临近甘陶河，推开房门映入眼帘的是甘陶河的风景，山和游船相呼应，在夜晚更深切的体会到古村落的寂静。荷塘月色院内装修均为榻榻米风格，院内面积25㎡左右，院内有四间民宿房，分别为长思、采莲、静坐、益养天年，每间客房面积均为25㎡左右，每间客房内都带有独立卫生间。纯净的天空，梦幻的远方，繁华之外，安静之上，或栖于村寨，享受原始与淳朴。'
        },
        {
            'src1': 'http://image.taocishuizhen.com/民宿/陶岸憩斋1.jpg',
            'src2': 'http://image.taocishuizhen.com/民宿/陶岸憩斋2.jpg',
            'name': '陶岸憩斋',
            'intro': '那多情的水、那别致的院、那古老的瓷窑，构成一幅陶瓷水镇独具特色的江南水乡水墨画卷。'
        },
        {
            'src1': 'http://image.taocishuizhen.com/民宿/迓祉迎祥1.jpg',
            'src2': 'http://image.taocishuizhen.com/民宿/迓祉迎祥2.jpg',
            'name': '迓祉迎祥',
            'intro': '沿街望去，青砖黛瓦，斗拱垂檐，宛若回到了梦里故乡。大红灯笼高高挂，“陶瓷水镇南横口”。真的是未见秀水，已然见波。'
        },
        {
            'src1': 'http://image.taocishuizhen.com/民宿/双河别墅1.jpg',
            'src2': 'http://image.taocishuizhen.com/民宿/双河别墅2.jpg',
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
            'src1': 'http://image.taocishuizhen.com/美食/ji.jpg',
            'src2': 'http://image.taocishuizhen.com/美食/1.jpg',
            'name': '村里那只鸡',
            'intro': ' 煮着鸡汤的铁锅边再围上一圈的玉米面饼子，盖上锅盖，铁锅中的蒸汽连同锅壁的温度一起将饼焖熟。焖好的饼松软可口，再配上一碗鲜美的鸡汤，这味道绝了！'
        },
        {
            'src1': 'http://image.taocishuizhen.com/美食/df.jpg',
            'src2': 'http://image.taocishuizhen.com/美食/1.jpg',
            'name': '水镇黑豆腐',
            'intro': ' 黑豆腐的制作是个手艺活，也是醉淳朴的坚守，当地的好山泉，制作不加石膏，全靠大石板压制出扎实而沉甸甸的豆腐，带着自然粗糙的气孔。除了糙实和灰色的外表，其实最让人会沉迷的，还是一股裹着豆香的炭火焦香，这气味会让人想起农村的大锅里烧出的饭菜香，不少人会在闻到这股独特豆香的时候被感动到。'
        },
        {
            'src1': 'http://image.taocishuizhen.com/美食/dgc.jpg',
            'src2': 'http://image.taocishuizhen.com/美食/1.jpg',
            'name': '大锅菜',
            'intro': ' 大锅菜又名熬菜，是一道色香味俱全的传统名菜，中国北方地区常见菜品之一，在北方地区较流行。食材多样，营养丰富，汤汁浓郁。此菜其名称的由来，首先是它有很多种菜的风味，其次就是说在早年大家是在一起吃饭一起干活，所以就叫做了大锅菜。'
        },
        {
            'src1': 'http://image.taocishuizhen.com/美食/yu.jpg',
            'src2': 'http://image.taocishuizhen.com/美食/1.jpg',
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
            'src1': 'http://image.taocishuizhen.com/伴手礼/1.jpg',
            'src2': 'http://image.taocishuizhen.com/伴手礼/2.jpg',
            'name': '茶叶罐',
            'intro': ' 茶叶是一种娇气的物品，稍保养不好就跑味，或者易潮，让原本原滋原味的茶叶变味，高档茶叶瞬间不值钱，陶瓷茶叶罐刚好弥补了这一缺陷，不但装茶叶能防潮，还让茶叶原味保持清香很久，茶叶一单装在茶叶罐里的时候，一下子提高茶叶的档次，让茶文化和陶瓷文化演绎的完美结合。'
        },
        {
            'src1': 'http://image.taocishuizhen.com/伴手礼/8.jpg',
            'src2': 'http://image.taocishuizhen.com/伴手礼/7.jpg',
            'name': '斗笠杯',
            'intro': ' 山水画中，凭江垂钓的渔翁，头上总是少不得一顶斗笠。因为斗笠是田园生活的缩影，宁静，安详，流露着一股自由闲适，不由让人心安，充满向往。'
        }
    ]
    return render(request, 'vacation/commodity.html', context)


def play(request):
    context = {}
    context['title'] = '休闲娱乐'
    context['cont'] = [
        {
            'src1': 'http://image.taocishuizhen.com/娱乐/tc1.jpg',
            'src2': 'http://image.taocishuizhen.com/娱乐/tc2.jpg',
            'name': '陶瓷体验馆',
            'intro': ' 在优雅古朴环境里，伴着悠扬的音乐，放松精神，仿佛置身世外桃源，来体验制作陶瓷'
        },
        {
            'src1': 'http://image.taocishuizhen.com/娱乐/hq.jpg',
            'src2': 'http://image.taocishuizhen.com/娱乐/hq1.jpg',
            'name': '呐喊喷泉',
            'intro': ' 网红呐喊喷泉不仅能“闻”声起舞，还能伴随呐喊声持续上升，声音越持久喷泉越高。如果你的肺活量爆棚的话，你将会看到这道水光与蓝天白云举案齐眉的壮观景象，惊叹它的神奇！在这样一个天然氧吧里放声呐喊，释放激情！释放压力!'
        },
        {
            'src1': 'http://image.taocishuizhen.com/娱乐/hf.jpg',
            'src2': 'http://image.taocishuizhen.com/娱乐/hf1.jpg',
            'name': '画舫',
            'intro': ' 艳唱潮初落，江花露未晞。春洲惊翡翠，朱服弄芳菲。画舫烟中浅，青阳日际微。锦帆冲浪湿，罗袖拂行衣。含情罢所采，相叹惜流晖。'
        },
        {
            'src1': 'http://image.taocishuizhen.com/娱乐/jtc.jpg',
            'src2': 'http://image.taocishuizhen.com/娱乐/jtc1.jpg',
            'name': '脚踏船',
            'intro': '集运动、娱乐、休闲等功能于一体，满足个人及家庭享受生活的需要。在发展中国家，脚踏船多作为公园、旅游景点的经营项目供人们消费，少量也作为个人的游玩手段。'
        },
        {
            'src1': 'http://image.taocishuizhen.com/娱乐/wpc.jpg',
            'src2': 'http://image.taocishuizhen.com/娱乐/wpc1.jpg',
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
            {"img": 'http://image.taocishuizhen.com/美食/ji.jpg',
             "p": ['煮着鸡汤的铁锅边再围上一圈的玉米面饼子，盖上锅盖，铁锅中的蒸汽连同锅壁的温度一起将饼焖熟。']
             },
            {"img": 'http://image.taocishuizhen.com/美食/1.jpg',
             "p": ['焖好的饼松软可口，再配上一碗鲜美的鸡汤，这味道绝了！']
             }],
        '水镇黑豆腐': [
            {"img": 'http://image.taocishuizhen.com/美食/df.jpg',
             "p": ['黑豆腐的制作是个手艺活，也是醉淳朴的坚守，当地的好山泉，制作不加石膏，全靠大石板压制出扎实而沉甸甸的豆腐，带着自然粗糙的气孔。']
             },
            {"img": 'http://image.taocishuizhen.com/美食/1.jpg',
             "p": ['除了糙实和灰色的外表，其实最让人会沉迷的，还是一股裹着豆香的炭火焦香，这气味会让人想起农村的大锅里烧出的饭菜香，不少人会在闻到这股独特豆香的时候被感动到。']
             }
        ],
        '大锅菜': [
            {"img": 'http://image.taocishuizhen.com/美食/dgc.jpg',
             "p": ['大锅菜又名熬菜，是一道色香味俱全的传统名菜，中国北方地区常见菜品之一，在北方地区较流行。食材多样，营养丰富，汤汁浓郁。']
             },
            {"img": 'http://image.taocishuizhen.com/美食/1.jpg',
             "p": ['此菜其名称的由来，首先是它有很多种菜的风味，其次就是说在早年大家是在一起吃饭一起干活，所以就叫做了大锅菜。']
             }
        ],
        '鱼和豆腐的故事': [
            {"img": 'http://image.taocishuizhen.com/美食/yu.jpg',
             "p": ['鱼和豆腐本是绝配，这道鳗鱼肉馅酿豆腐，既有鱼的鲜美，也有肉的丰腴，更有豆腐的清香，一口下去，回味无穷']
             },
            {"img": 'http://image.taocishuizhen.com/美食/1.jpg',
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
            {"img": 'http://image.taocishuizhen.com/民宿/马家大院1.jpg',
             "p": ['马家大院位于村子的正中央，是清代轶士马席珍的故居，历经一百多年的历史沧桑，仍旧矗立在这个古老的村庄。']
             },
            {"img": 'http://image.taocishuizhen.com/民宿/马家大院2.jpg',
             "p": ['整个院落古典而错落有致，华丽而不奢靡，在瓦片和屋檐下，烛光闪闪，想必有很多值得探索的故事！院内有三间民宿，分别为素雅、淳朴、勤勉，每间客房面积均为20㎡左右，每间客房内都带有独立卫生间。山景之中的日出，河韵之中的秀石，美景与远方，时光与情怀，享受与自在。']
             }],
        '忠孝传家': [
            {"img": 'http://image.taocishuizhen.com/民宿/忠孝传家1.jpg',
             "p": ['忠孝传家远，诗书继世长。忠孝传家院落是中式装修风格，院内共有三间民宿，院内配有厨房，三五好友，住在这样的院落，好不惬意。']
             },
            {"img": 'http://image.taocishuizhen.com/民宿/忠孝传家2.jpg',
             "p": ['院内面积30㎡左右，院内三间民宿分别为睿智、礼仪、仁慈义德，每间客房面积均在25㎡左右，配有公共卫生间。']
             }
        ],
        '永春堂萱': [
            {"img": 'http://image.taocishuizhen.com/民宿/永春堂萱1.jpg',
             "p": ['永春堂萱（一宅三院）民宿院内20㎡左右，院内有三间民宿，分别为清闲、安逸、甜淡，每间客房面积均为15㎡左右，三间客房公用卫生间。民宿，让赶路者放缓了脚步，在慢时光下懂得慢享受；']
             },
            {"img": 'http://image.taocishuizhen.com/民宿/永春堂萱2.jpg',
             "p": ['让旅行者为之倾倒，寻觅宁静中的那份洒脱；让寻梦者为之惊叹，如诗梦一样的经营生活。有形、有意、有境，民宿之美，美在年代感；民宿之美，美在有灵魂。']
             }
        ],
        '观陶水榭': [
            {"img": 'http://image.taocishuizhen.com/民宿/观陶水榭1.jpg',
             "p": ['观陶水榭民宿院位于一宅三院民宿院旁，民宿院内分为上下两层，装修都为中式风格，院内面积30㎡左右，院内有三间民宿房，分别为悟禅、静夜思、听风赏月，悟禅房间面积稍小，15㎡左右，静夜思和听风赏月面积均为30㎡左右，每间客房内都带有独立卫生间。']
             },
            {"img": 'http://image.taocishuizhen.com/民宿/观陶水榭2.jpg',
             "p": ['迷人的民宿，好似一家富有情怀的小酒馆，里面藏着各种美味的酒。休憩之日，与三五老友小聚一餐，醉人的佳酿入口，思绪慢慢的走，带你回到美好的年代']
             }
        ],
        '荷塘月色': [
            {"img": 'http://image.taocishuizhen.com/民宿/荷塘月色1.jpg',
             "p": [
                 '荷塘月色民宿院临近甘陶河，推开房门映入眼帘的是甘陶河的风景，山和游船相呼应，在夜晚更深切的体会到古村落的寂静。']
             },
            {"img": 'http://image.taocishuizhen.com/民宿/荷塘月色2.jpg',
             "p": ['荷塘月色院内装修均为榻榻米风格，院内面积25㎡左右，院内有四间民宿房，分别为长思、采莲、静坐、益养天年，每间客房面积均为25㎡左右，每间客房内都带有独立卫生间。纯净的天空，梦幻的远方，繁华之外，安静之上，或栖于村寨，享受原始与淳朴']
             }
        ],
        '陶岸憩斋': [
            {"img": 'http://image.taocishuizhen.com/民宿/陶岸憩斋1.jpg',
             "p": [
                 '陶岸憩斋是离景区中心较远的一处民宿院落。因所有的墙体建筑以及地面都使用烧瓷时用的耐火砖，而耐火砖的砖体表面颜色呈金黄色，故名为“黄金屋”。']
             },
            {"img": 'http://image.taocishuizhen.com/民宿/陶岸憩斋2.jpg',
             "p": ['院内面积40㎡左右，院内有四间民宿，分别为松、竹、美、兰，每间客房面积均为20㎡左右，每间客房内都带有独立卫生间。民宿或许是寻觅归属感的最佳地方，在这里可以让你摆脱都市压力的束缚，让疲惫的心灵得到宝贵的歇息机会，更重要的是可以找寻到久违的归属感，遇见最美的自己。']
             }
        ],
        '迓祉迎祥': [
            {"img": 'http://image.taocishuizhen.com/民宿/迓祉迎祥1.jpg',
             "p": [
                 '“迓，迎也。古本皆作讶。祉，福也，禄也。迎祥 ，迎纳吉祥。”']
             },
            {"img": 'http://image.taocishuizhen.com/民宿/迓祉迎祥2.jpg',
             "p": [
                 '迓祉迎祥院内面积20㎡左右，院内有三间民宿，分别为福瑞、祥和、厚德载物，每间客房面积均为17㎡左右，每间客房内都带有独立卫生间。行在胡同里，住在人情里。陶瓷水镇民宿，你来，春暖花开。']
             }
        ],
        '双河别墅': [
            {"img": 'http://image.taocishuizhen.com/民宿/双河别墅1.jpg',
             "p": [
                 '人生难得仙境处，陶瓷水镇在人间']
             },
            {"img": 'http://image.taocishuizhen.com/民宿/双河别墅2.jpg',
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
        '陶瓷体验馆': [
            {"img": 'http://image.taocishuizhen.com/娱乐/tc1.jpg',
             "p": ['在优雅古朴环境里，伴着悠扬的音乐，放松精神，仿佛置身世外桃源，来体验制作陶瓷']
             },
            {"img": 'http://image.taocishuizhen.com/娱乐/tc2.jpg',
             "p": ['在陶瓷体验馆整个体验流程分了三大部分，分别是拉坯、彩绘、捏雕。在这里，孩子们和泥土亲密接触，和同学一起动脑、动手，发挥自己的聪明才智，感受制陶的快乐。拉坯是将坯用的瓷泥团置于辘轳上，在辘轳转动中，用手和刮板把坯拉成所需要的形状；捏雕则是把泥团塑成自己想象到的自然形象；而彩绘是以陶瓷当纸，以特制的彩料当墨进行绘画，增加陶瓷的美感。瓷器是火的艺术，在制作过程中，人的心灵、精神和意志仿佛也经历了水的洗涤、泥的塑造、火的煅烧一般。通过制陶体验，既锻炼了孩子们的动手能力，又提高了想象力及创造力，同时也培养了孩子们热爱祖国传统文化的美好情感。我们作为家长，那份柔软和细腻还在，陪伴孩子，让人更直接的找回童趣和率真。']
             }],
        '呐喊喷泉': [
            {"img": 'http://image.taocishuizhen.com/娱乐/hq.jpg',
             "p": ['网红呐喊喷泉不仅能“闻”声起舞，还能伴随呐喊声持续上升，声音越持久喷泉越高。']
             },
            {"img": 'http://image.taocishuizhen.com/娱乐/hq1.jpg',
             "p": ['如果你的肺活量爆棚的话，你将会看到这道水光与蓝天白云举案齐眉的壮观景象，惊叹它的神奇！在这样一个天然氧吧里放声呐喊，释放激情！释放压力!']
             }],
        '画舫': [
            {"img": 'http://image.taocishuizhen.com/娱乐/hf.jpg',
             "p": ['艳唱潮初落，江花露未晞。春洲惊翡翠，朱服弄芳菲。']
             },
            {"img": 'http://image.taocishuizhen.com/娱乐/hf1.jpg',
             "p": ['画舫烟中浅，青阳日际微。锦帆冲浪湿，罗袖拂行衣。含情罢所采，相叹惜流晖。']
             }
        ],
        '脚踏船': [
            {"img": 'http://image.taocishuizhen.com/娱乐/jtc.jpg',
             "p": ['集运动、娱乐、休闲等功能于一体，满足个人及家庭享受生活的需要。']
             },
            {"img": 'http://image.taocishuizhen.com/娱乐/jtc1.jpg',
             "p": ['在发展中国家，脚踏船多作为公园、旅游景点的经营项目供人们消费，少量也作为个人的游玩手段。']
             }
        ],
        '乌篷船': [
            {"img": 'http://image.taocishuizhen.com/娱乐/wpc.jpg',
             "p": ['碧波漫透的水，乌篷船飘于上面，不禁令人想到无数的描写江南水乡的诗句，想到那诗情画意的地方。']
             },
            {"img": 'http://image.taocishuizhen.com/娱乐/wpc1.jpg',
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
            {"img": 'http://image.taocishuizhen.com/activity/lf1.jpg',
             "p": ['井陉窑是历经隋、唐、宋、金、元、明、清等朝代的一处大型瓷窑址集群，距今已有千年历史。南横口村位于井陉县城南部,是历史古村，井陉现代陶瓷业的发源地，遗存县内规模最大、保存最为完整的古瓷密遗址。南横口古瓷窑是井陉窑的重要组成部分和典型代表。作为石家庄市第五届旅发大会重要景点之一的陶瓷水镇，就是依托南横口村古瓷窑遗址片区重新规划而建。']
             },
            {"img": 'http://image.taocishuizhen.com/activity/lf2.jpg',
             "p": ['一进入陶瓷水镇，仿若置身于花海中的江南小镇，各种厨房里常见的砂锅、瓷碗、水瓮、菜坛等都被排列成各种造型，镶嵌在景区的景观墙上，古朴中透着雅致，古时人的厨房“旧爱”摇身一变成为了现代人的“新欢”，这些盆盆罐罐的装饰如此的别具一格，每一个新颖的造型都让人眼前一亮。陶瓷水镇把匣钵(笼盔)、陶砖植入古民居独有特点,赋予了南横口古民居独有的笼盔文化、红石文化和窑砖文化特征，置身其间,我们仿佛游润于一座露天瓷艺建筑博物馆。']
             }],
        '井陉古村落——陶瓷水镇新添红色文化主题展馆': [
            {"img": 'http://image.taocishuizhen.com/activity/hs2.jpg',
             "p": ['陶瓷水镇位于井陉县南横口村，是井陉县重点打造的一处集观光游览、休闲度假、创意文化、滨水娱乐等旅游业态为一体的山水休闲旅游度假景区。12月26日上午，景区精心打造的红色文化主题展馆举行了开展仪式，展馆展示的红色书籍、红色书画等千余件红色实物，吸引众多周围居民以及游客、学生等不同群体前来观展。']
             },
            {"img": 'http://image.taocishuizhen.com/activity/hs1.jpg',
             "p": ['同时也有效提升了陶瓷水镇的旅游文化产业发展，吸引了人气，让市民到陶瓷水镇旅游观光的同时，感受红色历史文化，激发大家干事创业的红色能量，引导人们特别是广大青少年切实增强历史使命感和责任感，更加珍惜现在的美好生活。']
             }
        ],
        '陶瓷水镇新貌即将亮相石家庄第五届旅发大会！': [
            {"img": 'http://image.taocishuizhen.com/activity/lf3.jpg',
             "p": ['作为石家庄市第五届旅发大会重要景点之一，按照旅发大会筹委会的总体规划设计，目前，南横口村陶瓷水镇景区各景点准备工作基本就绪，个别节点正在进一步精细化打造中。走进井陉县秀水镇南横口村陶瓷水镇，可以感受到这里的陶瓷文化。镶嵌在景观墙上的别致陶瓷造型、整齐排列的新颖盆罐、特制的巨型白瓷瓶景观......']
             },
            {"img": 'http://image.taocishuizhen.com/activity/lf4.jpg',
             "p": ['次旅发大会以“太行风情 古陉新韵”为主题，以“活旅游、聚产业、促发展、惠民生”为宗旨，依托井陉千年古县、百年老矿文化底蕴和生态资源优势，实施旅游公共服务设施提升工程、景区设施提档和新项目建设工程，丰富当地旅游资源，打造传统古村落片区。另外，大会期间，井陉拉花、花脸社火、苍岩龙鼓、秦皇古乐、锣架鼓、丝弦、竹马等国家级省级非遗节目将悉数亮相。']
             }
        ],
        '井陉陶瓷水镇民俗文化节启动': [
            {"img": 'http://image.taocishuizhen.com/activity/1.jpg',
             "p": [
                 '千年瓷韵展芳华，魅力水乡似江南。9月28日上午，由井陉县委宣传部主办，河北华秀文化旅游有限公司承办的“‘迎国庆’井陉陶瓷水镇民俗文化节”在位于井陉县秀林镇的“南横口陶瓷水镇”正式启动。当天上午，“遇见陶瓷水镇”抖音短视频大赛也一并启动。']
             },
            {"img": 'http://image.taocishuizhen.com/activity/whj2.jpg',
             "p": [
                 '文化节期间，不仅极具浓郁本土气息的拉花、社火等非物质文化遗产项目将悉数登台亮相，为游客奉上独特的文化大餐，而且缸炉烧饼等当地特色美食和来自全国各地的地方小吃也将持续刺激游客味蕾。文化节期间，不仅极具浓郁本土气息的拉花、社火等非物质文化遗产项目将悉数登台亮相，为游客奉上独特的文化大餐，而且缸炉烧饼等当地特色美食和来自全国各地的地方小吃也将持续刺激游客味蕾。利用当地古民居修旧如旧建成的古朴高端的精品民宿也将正式对外开放，让游客体验到独特的陶瓷风情民宿。']
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

def notice_detail(request, name):
    context = {}
    context['title'] = name + '|陶瓷水镇'
    context['title2'] = '更多公告'
    notice_list = {
        '井陉：陶瓷水镇南横口喜迎第四届省旅发大会观摩团': [
            {"img": 'http://image.taocishuizhen.com/activity/gm.jpg',
             "p": ['10月15日上午9时，第四届河北省旅游产业发展大会在石家庄国际会展中心开幕。10月16日上午旅发观摩团分两批来到井陉县陶瓷水镇南横口进行观摩。观摩团队按预定路线从东广场开始观摩。']
             },
            {"img": 'http://image.taocishuizhen.com/activity/gm2.bmp',
             "p": ['昨天夜间天气就下起了小雨，一直到观摩团到达观摩小雨没有丝毫“收敛”的意思。气温骤降，绵绵秋雨不停的散落在大家身上，但并没有影响到各个成员的兴致，大家表示没想到井陉还有这么好的地方。“闲暇之余我一定带我的家人到此好好转转，特色民宿住上一晚，体验一番”一位成员说到。']
             }],
        '文旅部、国家卫健委联合下发《通知》 严格规范景区管理': [
            {"img": 'http://image.taocishuizhen.com/activity/tz.jpg',
             "p": ['近日，文化和旅游部、国家卫生健康委两个部委联合印发《关于做好旅游景区疫情防控和安全有序开放工作的通知》，提出了加强景区疫情防控和有序开放的更严格、更详实的要求。这个通知在清明节和劳动节两个旅游重要节假期的中间档期，使旅游业暂缓键直指“五一”黄金周。']
             },
            {"img": 'http://image.taocishuizhen.com/activity/tz2.png',
             "p": ['《通知》明确，要坚持防控为先，实行限量开放。强调各地在做好旅游景区疫情防控工作的前提下，按照分区分级原则，严格落实《旅游景区恢复开放疫情防控措施指南》要求，做到限量开放、有序开放，严防无序开放。疫情防控期间，旅游景区只开放室外区域，室内场所暂不开放，接待游客量不得超过核定最大承载量的30％，收费景区在实施临时性优惠政策前要做好评估，防止客流量超限。《通知》要求，要强化流量管理，严防人员聚集。旅游景区要建立完善预约制度，推行分时段游览预约，引导游客间隔入园、错峰旅游，严格限制现场领票、购票游客数量，做好游客信息登记工作。要求各地严格落实旅游车辆防控安全，加强智慧旅游建设，做到旅游景区流量管理关口前置，严控客流。要细化管理措施，规范游览秩序。旅游景区要优化游览线路，在旅游景区出入口、重要参观点等容易形成人员聚集的区域配备必要的人员设备，严格落实体温筛检等防控措施，加强景区疏导和安全隐患排查，规范景区管理。《通知》强调，要加强组织领导，落实责任分工。各地要对旅游景区开放负主体责任，建立督导机制，切实加强旅游景区开放和旅游安全检查工作。要健全部门联动机制，落实落细防控责任，提高应急处置能力，及时妥善处理突发情况。各地要做好宣传引导，及时发布各类疫情防控指南和安全信息，引导游客遵守旅游活动中的安全警示规定，增强防护意识，配合防控工作，推进文明旅游。']
             }
        ],
        '旅游景区接待游客量不得超过核定最大承载量的30%...': [
            {"img": 'http://image.taocishuizhen.com/activity/cw1.jpg',
             "p": ['要求各地在做好旅游景区疫情防控工作的前提下，坚持分区分级原则，严格落实《旅游景区恢复开放疫情防控措施指南》要求，做到限量、有序开放，严防无序开放。疫情防控期间，旅游景区只开放室外区域，室内场所暂不开放；旅游景区接待游客量不得超过核定最大承载量的30%。收费景区在实施临时性优惠政策前要慎重做好评估，防止客流量超限。']
             },
            {"img": 'http://image.taocishuizhen.com/activity/cw2.jpg',
             "p": ['旅游景区要建立完善预约制度，通过即时通讯工具、手机客户端、景区官网、电话预约等多种渠道，推行分时段游览预约，引导游客间隔入园、错峰旅游。严格限制现场领票、购票游客数量；要配备必要人员设备，加强清洁消毒，严格落实体温筛检等防控措施，结合实际，配套使用“健康码”核验等手段。']
             }
        ],

        '关于进一步加强公共场所新冠肺炎疫情防控工作的通告...': [
            {"img": 'http://image.taocishuizhen.com/activity/tg1.jpg',
             "p": ['疫情未解除前，全县暂不开放影剧院、棋牌室、游艺厅、网吧、舞厅、酒吧、KTV、培训机构、室内游泳馆（池）、密闭场所或利用地下空间等通风条件较差的体育场馆或体育场馆部分区域，其余公共场所和经营单位开业开放视疫情发展情况决定。公共场所经营单位要落实疫情防控主体责任，要进一步完善疫情防控工作预案，严格落实各项防控措施。县卫健局和行业主管部门要加强监督检查，对防控措施落实不到位的立即责令整改，拒不整改的按相关法规要求停产停业。']
             },
            {"img": 'http://image.taocishuizhen.com/activity/tg2.bmp',
             "p": [
                 '农贸市场、商场、超市、酒店等要采取限制客流量、推荐顾客采取自助购物、自助结算等措施，有效缩短排队等候时间，减少人群聚集。客运站、火车站等公共交通工具要通过加强人员设备配备、科学调整登乘时间、增加服务通道等措施，尽量减少乘客等待、排队时间；要合理组织运力，乘客登乘后尽可能安排隔位、分散就坐，切实降低人员密度。各类公共场所要按规定做好物体表面清洁消毒，加强室内通风，完善手消毒设施配备，严格落实好各项环境卫生措施。要严格督促服务人员、顾客佩戴口罩，落实体温筛检措施，对于拒绝佩戴口罩、检测体温或出现发热、干咳等可疑症状的，应当劝阻进入场所或登乘公共交通工具，防止疫情传播。']
             }],
        '关于应对新冠肺炎疫情影响加快服务业发展的工作方案...': [
            {"img": 'http://image.taocishuizhen.com/activity/tg1.jpg',
             "p": [
                 '这一阶段是疫情防控的关键期。主要任务是在坚持打好疫情防控阻击战，同时推动服务业行业企业全面复工复业并实现正常经营，最大限度弥补疫情造成的损失，为全年服务业增长奠定基础。保障交通物流、快递业正常运行，确保生产生活资料正常运输。尽快组织企业复工复业，饭店烹饪、洗染美容美发等服务业态做到能开尽量开；适时有序推动沐浴、会展和文化旅游业等人员密集的行业恢复经营。大力提高行政效能，提高网上申报审批比例。加快项目推进进度，帮助项目解决建设存在的困难和问题。加快旅游景区升级改造，推动景区配套服务体系扩容提质，持续推进旅游厕所革命。']
             },
            {"img": 'http://image.taocishuizhen.com/activity/tg2.png',
             "p": [
                 '这一阶段是服务业发展最后冲刺阶段，主要任务是集中全市力量对服务业发展的主要行业、重大项目加快推进，力争完成全年服务业目标任务。抓好“双11”“双12”活动，加快发展特色消费。丰富文旅融合产品体系，加快建设一批文化创意、度假休闲综合体，培育一批与工业、体育、康养等业态融合发展的文化旅游项目。']
             }
        ],
        '复工复产后，企业、景区等公共场所的防疫措施如何做？...': [
            {"img": 'http://image.taocishuizhen.com/activity/ff1.jpg',
             "p": [
                 '首先做好卫生消毒。实施分区域分项目开放，对不符合开放条件的场所和容易形成人员聚集的项目，可先不开放或延后开放。及时对景区公共场所通风换气、对游乐设备等进行清洁消毒。景区公园内卫生间要配备洗手液。']
             },
            {"img": 'http://image.taocishuizhen.com/activity/ff2.jpg',
             "p": [
                 '其次，加强健康监测和管理。实行“一进一测一登记”制度，进入景区公园前须进行体温检测，严格落实“戴口罩、勤洗手、保距离”要求，科学分流疏导游客，设置服务咨询、游客排队1米防疫安全线，采取分时段安排游客入园，减少人员聚集。']
             }
        ]
    }
    more_data = []
    for item in notice_list:
        if item != name:
            more_data.append({'name': item, 'img': notice_list[item][0]['img']})
    context['data'] = notice_list[name]
    context['idname'] = '新闻动态'
    context['tname'] = 'notice'
    context['name'] = name
    context['more_data'] = more_data
    return render(request, 'activity/detail.html', context)

def commodity_detail(request, name):
    context = {}
    context['title'] = name + '|陶瓷水镇'
    context['title2'] = '更多伴手礼'
    commodity_list = {
        '茶叶罐': [
            {"img": 'http://image.taocishuizhen.com/伴手礼/2.jpg',
             "p": ['茶叶是一种娇气的物品，稍保养不好就跑味，或者易潮，让原本原滋原味的茶叶变味，高档茶叶瞬间不值钱，陶瓷茶叶罐刚好弥补了这一缺陷，']
             },
            {"img": 'http://image.taocishuizhen.com/伴手礼/1.jpg',
             "p": ['不但装茶叶能防潮，还让茶叶原味保持清香很久，茶叶一单装在茶叶罐里的时候，一下子提高茶叶的档次，让茶文化和陶瓷文化演绎的完美结合。']
             }],
        '斗笠杯': [
             {"img": 'http://image.taocishuizhen.com/伴手礼/8.jpg',
             "p": ['山水画中，凭江垂钓的渔翁，头上总是少不得一顶斗笠。因为斗笠是田园生活的缩影，宁静，安详，流露着一股自由闲适，不由让人心安，充满向往。']
             },
            {"img": 'http://image.taocishuizhen.com/伴手礼/7.jpg',
            "p": ['千百年来，精巧的斗笠杯碗也沾了斗笠的光，被古人赋予了一种逸然世外，天高云淡的道韵。甚至很多文人雅客认为用三才盖碗泡茶、斗笠杯品茶，才能充分体会茶道的韵。如今尚存的茶道流派，都对斗笠杯用情颇深。']
             }]

    }
    more_data = []
    for item in commodity_list:
        if item != name:
            more_data.append({'name': item, 'img': commodity_list[item][0]['img']})
    context['data'] = commodity_list[name]
    context['idname'] = '休闲娱乐'
    context['tname'] = 'commodity'
    context['name'] = name
    context['more_data'] = more_data
    return render(request, 'vacation/detail.html', context)

def activity_detail(request, name):
    context = {}
    context['title'] = name + '|陶瓷水镇'
    context['title2'] = '更多活动'
    activity_list = {
        '“迎国庆”井陉陶瓷水镇民俗文化节启动仪式': [
            {"img": 'http://image.taocishuizhen.com/activity/YGQ.jpg',
             "p": ['千年瓷韵展芳华，魅力水乡似江南。9月28日上午，河北华秀文化旅游有限公司“‘迎国庆’井陉陶瓷水镇民俗文化节”在位于省会西部甘陶、绵曼两河交汇处的南横口村正式启动。当天上午，“遇见陶瓷水镇”抖音短视频大赛也一并启动。']
             },
            {"img": 'http://image.taocishuizhen.com/activity/YGQ1.jpg',
             "p": ['迎国庆’井陉陶瓷水镇民俗文化节”是“南横口陶瓷水镇”在国庆节和河北省第四届旅游产业发展大会期间重点打造的特色文化项目，文化节将一直持续至10月16日。文化节期间，不仅极具浓郁本土气息的拉花、社火等非物质文化遗产项目将悉数登台亮相，为游客奉上独特的文化大餐。而且缸炉烧饼等当地特色美食和来自全国各地的地方小吃也将持续刺激游客味蕾，利用当地古民居修旧如旧建成的古朴高端的精品民宿也将正式对外开放，让游客体验到独特的陶瓷风情民宿。']
             }],
        '陶瓷水镇-社火表演': [
             {"img": 'http://image.taocishuizhen.com/activity/GMHD.jpg',
             "p": ['红脸社火是井陉一项国家级非物质遗产项目,今天也被请到景区,听大鼓响了,南广场演员被游客围成一个圈,看开打啦']
             },
            {"img": 'http://image.taocishuizhen.com/activity/GMHD1.jpg',
            "p": ['']
             }],
        '陶瓷水镇新貌即将亮相石家庄第五届旅发大会': [
            {"img": 'http://image.taocishuizhen.com/activity/JJLX.jpg',
             "p": [
                 '作为石家庄市第五届旅发大会重要景点之一，按照旅发大会筹委会的总体规划设计，目前，南横口村陶瓷水镇景区各景点准备工作基本就绪，个别节点正在进一步精细化打造中。走进井陉县秀水镇南横口村陶瓷水镇，可以感受到这里的陶瓷文化。镶嵌在景观墙上的别致陶瓷造型、整齐排列的新颖盆罐、特制的巨型白瓷瓶景观......']
             },
            {"img": 'http://image.taocishuizhen.com/activity/JJLX1.jpg',
             "p": [
                 '石家庄游客汤雨在朋友推荐下第一次来到南横口村陶瓷水镇，古镇新貌让她眼前一亮：“印象中井陉是落后的山区，没想到这里有如此好的自然和文化资源，能感受原生态的古镇风貌，很轻松、很惬意。本次旅发大会以“太行风情 古陉新韵”为主题，以“活旅游、聚产业、促发展、惠民生”为宗旨，依托井陉千年古县、百年老矿文化底蕴和生态资源优势，实施旅游公共服务设施提升工程、景区设施提档和新项目建设工程，丰富当地旅游资源，打造传统古村落片区。”']
             }],
        '陶瓷水镇红色文化主题展馆举行开展仪式': [
            {"img": 'http://image.taocishuizhen.com/activity/HSWH.jpg',
             "p": [
                 '陶瓷水镇位于井陉县南横口村，是井陉县重点打造的一处集观光游览、休闲度假、创意文化、滨水娱乐等旅游业态为一体的山水休闲旅游度假景区。12月26日上午，景区精心打造的红色文化主题展馆举行了开展仪式，展馆展示的红色书籍、红色书画等千余件红色实物，吸引众多周围居民以及游客、学生等不同群体前来观展。']
             },
            {"img": 'http://image.taocishuizhen.com/activity/HSWH1.jpg',
             "p": [
                 '“我们在陶瓷水镇建设这个展馆就是为了回望历史，缅怀先烈，传承发扬老区的红色精神，同时以史为鉴，汲取砥砺前行的强大力量。”展馆的建成为传承红色文化、发掘和保护好革命先辈们留下的宝贵资源起到了积极作用，同时也有效提升了陶瓷水镇的旅游文化产业发展，吸引了人气，让市民到陶瓷水镇旅游观光的同时，感受红色历史文化，激发大家干事创业的红色能量，引导人们特别是广大青少年切实增强历史使命感和责任感，更加珍惜现在的美好生活。']
             }],
        '曾经杭州西湖断桥爱情美，如今河北陶瓷水镇迎恋情': [
            {"img": 'http://image.taocishuizhen.com/activity/XQH.jpg',
             "p": [
                 '深秋的细雨缠缠绵绵飘落下来，朦朦胧胧的轻雾笼罩着爱情初体验的男男女女。剪不断的丝丝情雨似红娘的爱手为幸福牵连。近百名来自省会的男女参加了今天美丽陶瓷水镇牵手闯关、相亲活动。此时，不由地联想到白娘子与许仙的爱情故事，他们是西湖、断桥、雨天；今天我们在水镇、小桥、雨中']
             },
            {"img": 'http://image.taocishuizhen.com/activity/XQH1.jpg',
             "p": [
                 '爱情就是一次旅途，要去的地方名字叫做“幸福”。遇见谁都是一个美丽的意外，将压力与不良心绪格式化，释放快乐因子，抚慰躁动的心，携手闯关，画舫中汉服美女巧笑嫣然与岸边男子互动，体验制作陶瓷工艺，共同见证爱情初体验。']
             }]

    }
    more_data = []
    for item in activity_list:
        if item != name:
            more_data.append({'name': item, 'img': activity_list[item][0]['img']})
    context['data'] = activity_list[name]
    context['idname'] = '景区活动'
    context['tname'] = 'activity'
    context['name'] = name
    context['more_data'] = more_data
    return render(request, 'activity/detail.html', context)

def strategy_detail(request, name):
    context = {}
    context['title'] = name + '|陶瓷水镇'
    context['title2'] = '更多攻略'
    strategy_list = {
        '陶瓷水镇——带上好心情出发吧！！！': [
            {"img": 'http://image.taocishuizhen.com/trip/neirong1.jpg',
             "p": ['古风古色，陶瓷砖瓦搭建的墙壁，也不知道多少是新修，多少是原本的面貌了，但是走在窄窄的巷子里，高高低低的陡峭，还是体会的到曾经古老的生活。']
             },
            {"img": 'http://image.taocishuizhen.com/trip/neirong2.jpg',
             "p": ['疫情期间，人不算很多，有两三家可以吃饭，有小卖部可以买东西，走进民宿，可以看到每间得装修风格都截然不同，在院子里还能看到烧烤设备，想必这里的夜景也很美吧。陶瓷水镇，可以划船，可以放风筝，可以玩水，可以徒步，还可以体验制作陶瓷，满足全家人的需求了！！！']
             }],
        '石家庄周边游古村落篇—南横口陶瓷水镇': [
            {"img": 'http://image.taocishuizhen.com/trip/neirong3.jpg',
             "p": ['从去年的旅发大会我就听说井陉有个陶瓷水镇，今天终于有机会来陶瓷水镇啦... ... 陶瓷水镇位于井陉县南横口村，是具有特色历史遗留的古村落。一进入陶瓷小镇，各种厨房里常见的砂锅、瓷碗、水翁、菜坛，都被摆成各种造型，镶嵌在景区的景观墙上对于喜欢喜欢小瓷器的我，无疑是最大的吸引力。']
             },
            {"img": 'http://image.taocishuizhen.com/trip/neirong4.jpg',
             "p": [
                 '疫情期间，人不算很多，有两三家可以吃饭，有小卖部可以买东西，走进民宿，可以看到每间得装修风格都截然不同，在院子里还能看到烧烤设备，想必这里的夜景也很美吧。陶瓷水镇，可以划船，可以放风筝，可以玩水，可以徒步，还可以体验制作陶瓷，满足全家人的需求了！！！']
             },
            {"img": 'http://image.taocishuizhen.com/trip/neirong5.jpg',
             "p": [
                 '陶瓷水镇把笼盔、陶瓷植入古民居独有特点，赋予了南横口居民独有的笼盔文化。红石文化和窑砖文化特征，置身其间，仿佛游润于一座露天瓷艺建筑博物馆。笼盔垒墙，窑洞为家，清幽古道散发着千年古窑的气息！']
             }],
        '井陉有个南横口，凭水临风。': [
            {"img": 'http://image.taocishuizhen.com/trip/neirong7.jpg',
             "p": [
                 '陶瓷水镇千年古村，不仅是有着千年历史的传统古村落，还是陶瓷之乡。其实有水的地方都会很美，水总赋予大自然更多的灵性。近处，水面随风荡漾，偶尔有白鹅和野鸭游过；远处，山色清浅，火车不时隆隆而过。']
             },
            {"img": 'http://image.taocishuizhen.com/trip/neirong8.jpg',
             "p": [
                 '空气很好，水很干净，古香古色，疫情期间，人也并不是很多。看景，玩水，赏花，人文，都是不错的选择。']
             }],
        '周末野游': [
            {"img": 'http://image.taocishuizhen.com/trip/NR1.jpg',
             "p": [
                 '开到周末了，给大家推荐一个游玩好去处，井陉陶瓷水镇，古朴风格。水镇很纯朴，原来的一个民窑，以各式陶瓷装饰为主的风格，适合一家人轻松游玩。']
             },
            {"img": 'http://image.taocishuizhen.com/trip/NR2.jpg',
             "p": [
                 '甘陶河可以划船，有画舫、乌篷船、脚踏船都可以游玩，还可以看到白鹅，在这个特殊的时期我们可以选择食物进行野餐，当然景区也有主题餐厅，里面有很多井陉特色的美食。']
             },
            {"img": 'http://image.taocishuizhen.com/trip/NR3.jpg',
             "p": [
                 '陶瓷水镇还可以体验制作陶瓷，DIY一个自己专属的茶杯。世界这么大，不能一一走过，真正享受的是与家人一起，在这个陶瓷水镇，依然开心满足。']
             }],
        '有山有水的好地方': [
            {"img": 'http://image.taocishuizhen.com/trip/NR4.jpg',
             "p": [
                 '有山有水的地方一直是我心中向往的，美景怡人，特殊时期，人不是很多，对于喜静的人来说刚刚好，现在正是最适合来这里的季节！']
             },
            {"img": 'http://image.taocishuizhen.com/trip/NR5.jpg',
             "p": [
                 '天鹅在水上嬉戏玩闹，走在桥上，凉凉的风吹散了耳边的鬓发，一个人的感觉很奇妙，明明很孤单但在那一刻又好像拥有了整个世界。']
             },
            {"img": 'http://image.taocishuizhen.com/trip/NR6.jpg',
             "p": [
                 '在这里有井陉窑南横口的陶瓷品展示，也可以当做是纪念品来买卖，价格也很实惠，也可以自己亲手体验制作陶瓷。陶瓷水镇也有主题餐厅，可以品尝到当地特色美食。美食，风景与身边的人一起，这就是人生的一种满足吧！']
             }

        ],
        '陶瓷水镇游记': [
            {"img": 'http://image.taocishuizhen.com/trip/NR7.jpg',
             "p": [
                 '邢窑、定窑、磁州窑、井陉窑被称为河北四大名窑，在中国瓷器文化的历史长河中为河北留下了灿烂身影。而井陉窑最具代表性的就是南横口。中国古镇不少，我们省的西邻山西便以乔家大院、王家大院、平遥古城等闻名华夏，然而我庄里也有一县古镇极多，不下山西。那就是环“井陉天路”古镇圈。而这数十个古镇里中，以陶瓷水镇最具特色。']
             },
            {"img": 'http://image.taocishuizhen.com/trip/NR8.jpg',
             "p": [
                 '走近陶瓷水镇，了解井陉古窑的历史传承，古镇内的名人雅事，从或是依然傲然挺立，或是已经破败的断垣残壁中品位出历史的底蕴。陶瓷，这个让西方命名了中国的东西，将水、火、泥土完美的融合，从泥坯的软弱暗淡再到陶瓷的刚直明丽，是一种升华与精炼。中国的上古传说，女娲捏泥造人，而今英文之中中国与陶瓷为同一单词，一个是我们自己前人的传说，一个是西方的约定俗成，居然在陶瓷上碰撞到了一起，真有些冥冥之中自有天意的意味。燕赵自古多慷慨悲歌之士，宁为玉碎不为瓦全。而陶瓷更将这种品质发挥的淋漓尽致，不惧水火，却绝刚直不阿，宁可碎落成片，也绝不会改变初型。']
             },
            {"img": 'http://image.taocishuizhen.com/trip/NR9.jpg',
             "p": [
                 '自石市市区出发，不到一小时，便到南横口。果然是一风水宝地，太行东南环抱，治河临镇而过。南侧陶瓷水镇游客中心周围，有大片的花海。此时正迎河北第五届旅发大会，摆出了许多造型。沿东侧小路而下，未到古镇，便到了一处写着“毛主席万岁”和“为人民服务”的建筑之前。此建筑非常奇特，下方仿佛是一条巨蛇直冲而上，而长蛇顶被一间防止“镇压”。原来这处叫“民主渠倒吸虹”，具体是干啥的请依字面理解。']
             }

        ],

    }
    more_data = []
    for item in strategy_list:
        if item != name:
            more_data.append({'name': item, 'img': strategy_list[item][0]['img']})
    context['data'] = strategy_list[name]
    context['idname'] = '旅游攻略'
    context['tname'] = 'strategy'
    context['name'] = name
    context['more_data'] = more_data
    return render(request, 'trip/detail.html', context)

