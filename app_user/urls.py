from django.urls import path
from .views import Home
from . import views

urlpatterns = [
    path('home/', Home.as_view(), name='home'),
    path('home/user_info', views.user_info, name='user_info'),

]