"""TCSZWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
import tcsz.views as tcsz
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponse
urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^hello$', tcsz.hello),
    path('hello/',tcsz.hello),
    path('', tcsz.index, name='index'),
    path('test',tcsz.test),
    path('tradition/', tcsz.tradition),
    path('origin/', tcsz.origin),
    path('celebrity/', tcsz.celebrity),
    path('custom/', tcsz.custom),
    path('activity/', tcsz.activity),
    path('new/', tcsz.new),
    path('notice/', tcsz.notice),
    path('vacation/accommodation',tcsz.accommodation),
    path('vacation/food',tcsz.food),
    path('vacation/play',tcsz.play),
    path('vacation/commodity',tcsz.commodity),
    path('trip/service',tcsz.service),
    path('vacation/food/detail/<str:name>',tcsz.food_detail),
    path('vacation/commodity/detail/<str:name>',tcsz.commodity_detail),
    path('vacation/accommodation/detail/<str:name>', tcsz.accommodation_detail),
    path('vacation/play/detail/<str:name>', tcsz.play_detail),
    path('activity/new/detail/<str:name>', tcsz.new_detail),
    path('activity/notice/detail/<str:name>', tcsz.notice_detail),
    path('trip/strategy/detail/<str:name>', tcsz.strategy_detail),
    path('trip/strategy/detail/<str:name>', tcsz.strategy_detail),
    path('activity/activity/detail/<str:name>', tcsz.activity_detail),
    path('trip/traffic',tcsz.traffic),
    path('trip/strategy',tcsz.strategy),
    path('video/video',tcsz.video),
    path('mobile/', tcsz.mobile),
    path('mobile/scenic_overview', tcsz.scenic_overview),
    path('mobile/court_travel', tcsz.court_travel),
    path('mobile/comfortable', tcsz.comfortable),
    path('mobile/news', tcsz.news),
    path('mobile/contact', tcsz.contact),
    path('mobile/news_show/HS', tcsz.HS),
    path('mobile/news_show/TC', tcsz.TC),
    path('mobile/news_show/SH', tcsz.SH),
    path('mobile/news_show/SZ', tcsz.SZ),
    path('mobile/news_show/TSJ', tcsz.TSJ),
    url(r'^robots\.txt$', lambda r: HttpResponse('User-agent: *\nDisallow: /admin', content_type='text/plain')),

]+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
