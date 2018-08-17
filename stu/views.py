# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from models import *
# Create your views here.
from stu.forms import ChangepwdForm
from stu.models import User


def base_index(request):
    return render(request , 'base.html')

def login_index(request):
    uname=request.POST.get('uname','')
    return render(request,'container.html')

#注册
def register_index(request):

    if request.method=='GET':
        return render(request,'userRegistration.html')

    else:
        uaccount=request.POST.get('uaccount','')
        upwd=request.POST.get('upwd','')
        uphone=request.POST.get('uphone','')
        uemail=request.POST.get('uemail','')
        uphone=int(uphone)
        try:
            User.objects.get(uaccount=uaccount,upwd=upwd,uemail=uemail,uphone=uphone)
        except User.DoesNotExist:
            User.objects.create(uaccount=uaccount, upwd=upwd, uemail=uemail, uphone=uphone)
            response = HttpResponse('<script>alter(注册成功！！！)</script>')
            response.status_code = 302
            response.setdefault('Location', '/stu/login/')
            return response

        response = HttpResponse('<script>alter(注册失败！！！)</script>')
        response.status_code = 302
        response.setdefault('Location', '/stu/register/')
        return response

#账户唯一效验
def existView(request):
    #接收请求参数
    uaccount = request.GET.get('uname','')

    #判断数据库中是否存在
    userList = User.objects.filter(uaccount=uaccount)

    if userList:
        return JsonResponse({'flag':True})
    return JsonResponse({'flag':False})


def home_view(request):
    return render(request,'middle.html')

#更改密码
def updatePwd_index(request):
    if request.method=='POST':
        form=ChangepwdForm(request.POST)
        newpassword=request.POST.get('newPassword')
        oldpassword=request.POST.get('oldPassword')
        return  render(request,'changePwd.html',{'newpassword':newpassword,'oldpassword':oldpassword})
    else:
        form = ChangepwdForm
        return render(request,'changePwd.html',{'form':form})



def bookQuery_index(request):

    return render(request, 'bookQuery.html')



def bookBorrow_index(request):
    return render(request,'bookBorrow.html')



def bookBack_index(request):
    return render(request,'bookBack.html')


def bookBorrowState_index(request):
    return render(request,'bookBorrowState.html')

def first_index(request):
    username=request.session.get('username')
    return render(request, 'first.html', {'username':username})

def query_index(request):
    username = request.session.get('username')
    return render(request,'bookQuery.html',{'username':username})

def borrow_index(request):
    username = request.session.get('username')
    return render(request, 'bookBorrow.html', {'username': username})

def back_index(request):
    username = request.session.get('username')
    return render(request, 'bookBack.html', {'username': username})


def status_index(request):
    return render(request,'bookBorrowState.html')


def change_index(request):
    username = request.session.get('username')
    return render(request, 'changePwd.html', {'username': username})



def base_index(request):
    username=request.session.get('username')
    return render(request,'base.html',{'username':username})


def login_index(request):
    return render(request,'login.html')




def jiaoyan_index(request):
    username=request.POST.get('username')
    request.session['username']=username
    return render(request,'first.html',{'username':username})


def jieyueshuji_index(request):
    inum = request.GET.get('inum', '')
    inum = int(inum)
    username=request.session.get('username')
    user=User.objects.get(uname=username)
    information = Information.objects.get(inum=inum)
    try:
        bookBorrowing=BookBorrowing.objects.get(bnumber=inum)
        if bookBorrowing:
            message='您已经借阅该书籍'
    except BookBorrowing.DoesNotExist:
        bookBorrowing=BookBorrowing.objects.create(bid=1,bname=username,bnumber=inum,binfo=information,buser=user)
        if bookBorrowing:
            message='借阅成功'
            return JsonResponse({'flag': message})
    return JsonResponse({'flag':message})
    # return JsonResponse({'flag': False})

