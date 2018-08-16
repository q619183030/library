#coding=utf-8

from django.conf.urls import url
import views

urlpatterns=[
    url(r'^base/$',views.base_index),
    url(r'^login/$',views.login_index),
    url(r'^register/$',views.register_index),
    url(r'^home/$',views.home_view),


]