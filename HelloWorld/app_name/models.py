# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
# 新建了一个Student类，继承自models.Model
class Student(models.Model):
    name = models.CharField(max_length=128)
    age = models.IntegerField(max_length=3)

# # 插入数据
# class Student(models.Model):
#         Student.objects.create(name='lizili',age=18)
#         Student.objects.create(name='vic',age=22)
#         Student.objects.create(name='zhang',age=12)
#
# # 返回数据
#     def __str__(self):  #固定格式
#         return u'name: %s , age:%s' % (self.name,self.age)