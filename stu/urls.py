#coding=utf-8

from django.conf.urls import url
import views

urlpatterns=[
    url(r'^base/$',views.base_index),
    url(r'^login/$',views.login_index),
    url(r'^register/$',views.register_index),

    url(r'^home/$',views.home_view),
    url(r'^updatepwd/$', views.updatePwd_index),

    url(r'^bookBack/$',views.bookBack_index),
    url(r'^bookBorrow/$',views.bookBorrow_index),
    url(r'^bookBorrowState/$',views.bookBorrowState_index),
    url(r'^bookQuery/$',views.bookQuery_index),


]