# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


#普通用户表
class User(models.Model):
    uname=models.CharField(max_length=10)
    uaccount=models.CharField(max_length=30)
    upwd=models.CharField(max_length=50)
    uphone=models.PositiveIntegerField()
    uemail=models.EmailField()
    unum=models.PositiveIntegerField()

    class Meta:
        db_table='T_user'

    def __unicode__(self):
        return u'User.%s'%self.uname

#管理员表
class Administrator(models.Model):
    aname=models.CharField(max_length=30)
    account=models.CharField(max_length=20)
    apwd=models.CharField(max_length=50)
    aphone=models.PositiveIntegerField()
    aemail=models.EmailField()

    class Meta:
        db_table='T_administrator'

    def __unicode__(self):
        return u'Administrator.%s'%self.aname

# 图书类别表
class BookClass(models.Model):
    cname = models.CharField(max_length=20)
    clocation = models.CharField(max_length=30)

    class Meta:
        db_table = 'T_bookclass'

    def __unicode__(self):
        return u'BookClass.%s' % self.cname

#图书信息
class Information(models.Model):
    inum=models.CharField(max_length=20,primary_key=True,unique=True)
    iname=models.CharField(max_length=30)
    iauthor=models.CharField(max_length=20)
    ipublish=models.CharField(max_length=30)
    intro=models.TextField()
    itype=models.CharField(max_length=20)
    iprice=models.DecimalField( max_digits=3,decimal_places=2)
    iamount=models.PositiveIntegerField()
    #BookClass外键
    bookclass=models.ForeignKey(BookClass)

    class Meta:
        db_table='T_information'

    def __unicode__(self):
        return u'Information.%s'%self.iname




#图书借阅表
class BookBorrowing(models.Model):
    bid=models.PositiveIntegerField()
    bname=models.CharField(max_length=30)
    bnumber=models.PositiveIntegerField()
    borrow=models.DateField(auto_now_add=True)
    # back=models.TimeField()
    #Information外键
    binfo=models.ForeignKey(Information)
    #User外键
    buser=models.ForeignKey(User)

    class Meta:
        db_table='T_bookborrowing'

    def __unicode__(self):
        return u'user:%s,booknum:%s,btime:%s'%(self.bname,self.bnumber,self.borrow)

