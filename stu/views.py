# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from models import *
# Create your views here.
from stu.forms import ChangepwdForm
from stu.models import User


def base_index(request):
    return render(request,'base.html')

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
        if uaccount and upwd and uphone and uemail:
            try:
                User.objects.get(uaccount=uaccount,upwd=upwd,uphone=uphone,uemail=uemail)
            except User.DoesNotExist:
                User.objects.create(uaccount=uaccount,upwd=upwd,uphone=uphone,uemail=uemail)
            response = HttpResponse('<script>alter(注册成功！！！)</script>')
            response.status_code = 302
            response.setdefault('Location','/stu/login/')
            return response
        return HttpResponse('<script>alter(注册失败！！！)</script>，/stu/register/')

#唯一效验
def existView(request):
    #接收请求参数
    uaccount = request.GET.get('uaccount','')

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

<<<<<<< Updated upstream
=======
    return None


def bookQuery_index(request):

    return render(request, 'bookQuery.html')


def bookBorrow_index(request):
    return None



def bookBack_index(request):
    return render(request,'bookBack.html')


def bookBorrowState_index(request):
    return None
>>>>>>> Stashed changes
