# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import math
from django.core.paginator import Paginator
from django.db.models import *
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.core import serializers

from stu.models import *

def home_view(request):
    username = request.POST.get('username', '')
    pwd = request.POST.get('password', '')
    print username
    print pwd
    if username == 'zhangsan' and pwd == '123':
        request.session['username'] = username
        return render(request, 'home.html', {"username": username})
    return render(request, 'login.html')

def manager_index(request):
    return render(request,'base.html')


def oprateBook_view(request):
    return render(request,'oprateBook.html')



def get_post_by_num(num):
    num = int(num)
    page_info = Paginator(BookBorrowing.objects.order_by("-borrow"), per_page=1)
    begin = (num - int(math.ceil(10.0 / 2)))
    if begin < 1:
        begin = 1
    end = begin + 9
    if end > page_info.num_pages:
        end = page_info.num_pages
    if end <= 10:
        begin = 1
    else:
        begin = end - 9
    pagelist = range(begin, end + 1)
    return page_info.page(num), pagelist

def searchAll_view(request,num='1'):
    page_info, page_range = get_post_by_num(num)
    return  render(request,'searchAllBorrow.html',{'page_info':page_info,'page_range':page_range})


def addBooks_view(request):
    inum=request.POST.get('inum','')
    iname=request.POST.get('iname','')
    iauthor=request.POST.get('iauthor','')
    ipublish=request.POST.get('ipublish','')
    intro=request.POST.get('intro','')
    iprice=request.POST.get('iprice','')
    iamount=request.POST.get('iamount','')
    bookclass=request.POST.get('bookclass','')
    bookcls=BookClass.objects.filter(cname=bookclass)
    for f in bookcls:
        try:
            bookcls=BookClass.objects.get(id=f.id)
        except:
            pass
        try:
            book=Information.objects.get(inum=inum)
        except:
            book=Information.objects.create(inum=inum,iname=iname,iauthor=iauthor,ipublish=ipublish,intro=intro,iprice=iprice,iamount=iamount,bookclass=bookcls)
    return render(request,'addBooks.html')


def updatePwd_view(request):

    return render(request,'updatePwd.html')


def login_view(request):
    return render(request,'login.html')


def showMenu_view(request):
    bookname=request.GET.get('bookname')
    bookList1 = Information.objects.filter(iname=bookname)
    jBookList1 = serializers.serialize('json', bookList1)
    author = request.GET.get('author')
    bookList2 = Information.objects.filter(iauthor=author)
    jBookList2 = serializers.serialize('json', bookList2)
    return JsonResponse({'jBookList1': jBookList1,'jBookList2':jBookList2})