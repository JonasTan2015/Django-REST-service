from django.conf.urls import url, include
from django.contrib import admin
from DBAPI import views

urlpatterns = [
    url(r'db/$', views.hello),
    url(r'db/create', views.get_post_CreditCard, name='create_credit_card'),
    url(r'db/alchemycreate', views.create_AlchemyCreditCard, name='create_alchemyCreditCard')
]