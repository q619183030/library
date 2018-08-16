# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def base_index(request):
    return render(request,'base.html')

def login_index(request):
    return render(request,'container.html')


def register_index(request):
    if request.method=='GET':
        return render(request,'userRegistration.html')

    else:
        uaccount=request.POST.get('uaccount','')
        upwd=request.POST.get('upwd','')
        uphone=request.POST.get('uphone','')
        uemail=request.POST.get('uemail','')
        # if uaccount and upwd

    return None