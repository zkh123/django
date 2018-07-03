# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from app_name.models import Student

# Create your views here.


'''
http://127.0.0.1:8000/app/home/
'''


def home(request):
    context = {}
    context['hello'] = 'hello world!'
    return render(request, 'home.html', context)


# 查询，展示
'''
http://127.0.0.1:8000/app/select/
'''


def test(request):
    student_list = Student.objects.all().values()
    jsonData = serializers.serialize("json", student_list)  # 将queryset对象转换成json类型
    return HttpResponse(jsonData, content_type="application/json")


# 新增数据
'''
http://127.0.0.1:8000/app/add/
'''


def add(request):
    Student.objects.create(name='lizili', age=18)
    Student.objects.create(name='vic', age=22)
    Student.objects.create(name='zhang', age=12)
    return HttpResponse('ok')
