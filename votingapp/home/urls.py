from django.contrib import admin
from django.urls import include, path
from home import views
urlpatterns = [

path('', views.home, name='home'),
path('signup',views.signup,name='signup'),
path('login',views.login,name='login'),



]