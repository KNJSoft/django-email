from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.send,name='send' ),
    path('email/',views.mail,name='mail')
]