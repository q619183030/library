#coding=utf-8
from django.conf.urls import url

from manager import views

urlpatterns=[
    url(r'^$',views.manager_index)
]