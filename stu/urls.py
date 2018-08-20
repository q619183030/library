#coding=utf-8

from django.conf.urls import url
import views

urlpatterns=[
    url(r'^base/$',views.base_index),
    url(r'^login/$',views.login_index),
    url(r'^register/$',views.register_index),
    url(r'^exist/$',views.existView),
    url(r'^home/$',views.home_view),
    url(r'^updatepwd/$', views.updatePwd_index),
    url(r'^bookBack/$',views.bookBack_index),
    url(r'^bookBorrow/$',views.bookBorrow_index),
    url(r'^bookBorrowState/$',views.bookBorrowState_index),
    url(r'^bookQuery/$',views.bookQuery_index),
    url(r'^first/$',views.first_index),
    url(r'^query/$', views.query_index),
    url(r'^borrow/$', views.borrow_index),
    url(r'^back/$', views.back_index),
    url(r'^status/$', views.status_index),
    url(r'^change/$', views.change_index),
    url(r'^jiaoyan/$', views.jiaoyan_index),
    url(r'^borrow/(\d+)$', views.borrow_index),
    url(r'^jieyueshuji/$', views.jieyueshuji_index),
    url(r'^reLoadBook/(.*)', views.reLoadBook),
    url(r'^returnBook/(.*)', views.returnBook),

]