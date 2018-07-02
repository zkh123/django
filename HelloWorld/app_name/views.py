# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


'''
http://127.0.0.1:8000/app/home/
'''
def home(request):
    context = {}
    context['hello'] = 'hello world!'
    return render(request, 'home.html',context)