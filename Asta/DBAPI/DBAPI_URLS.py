from django.conf.urls import url, include
from django.contrib import admin
from DBAPI import views

urlpatterns = [

    url(r'/db', views.hello),
]