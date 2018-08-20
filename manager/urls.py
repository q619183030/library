#coding=utf-8
from django.conf.urls import url

from manager import views

urlpatterns=[
    url(r'^$',views.manager_index),
    url(r'^login/$', views.login_view),
    url(r'^home/$', views.home_view),
    url(r'^showMenu/$', views.showMenu_view),
    url(r'^opratebook/$', views.oprateBook_view),
    url(r'^searchall/$', views.searchAll_view),
    url(r'^addbooks/$', views.addBooks_view),
    url(r'^updatepwd/$', views.updatePwd_view),

]