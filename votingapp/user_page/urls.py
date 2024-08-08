from django.contrib import admin
from django.urls import include, path
from user_page import views
urlpatterns = [

path('', views.page, name='page'),
path('vote',views.vote,name='vote'),
path('result',views.result,name='result')
]