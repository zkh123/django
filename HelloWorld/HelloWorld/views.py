# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse

# Create your views here.


'''
http://127.0.0.1:8000/hs
'''


def hs(request):
    return HttpResponse('ok')
