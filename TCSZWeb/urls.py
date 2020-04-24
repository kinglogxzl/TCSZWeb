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
    path('vacation/accommodation/detail/<str:name>', tcsz.accommodation_detail),
    path('vacation/play/detail/<str:name>', tcsz.play_detail),
    path('trip/traffic',tcsz.traffic),
    path('trip/strategy',tcsz.strategy),
    path('video/video',tcsz.video)
]+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
