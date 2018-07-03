from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.home),  # new
    url(r'^select/', views.test),
    url(r'^add/', views.add),
]