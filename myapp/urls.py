"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from myapp import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^$', views.index),#用$符号(结束符号)，表示 什么path都不写，默认访问到主界面
    url(r'^login$|jj$|kk$', views.duoge), # ｜ 可以多个路径指向一个资源
    url(r'^aa/gouwuche/', views.tb),
    url(r'^loginpage/', views.login),
    url(r'^request1/', views.request1),
    url(r'^doRegist/', views.doRegist),
    url(r'^cha/', views.cha),
    url(r'^delete/', views.delete),
    url(r'^update/', views.update),
    url(r'^add/', views.add),
    url(r'^info/', views.info),
    url(r'^ifpd/', views.ifpd),








    url(r'^.', views.wanneng),# . 不管访问啥都是我，可以用来提示路径错误 这个一般情况放到最下面，
]
