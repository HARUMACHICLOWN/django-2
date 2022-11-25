
from django.urls import path
from userProject import views

urlpatterns = [
    path('index', views.index),
    path('error', views.error_page),
    path('user_info', views.user_info),
    path('user_info/<slug:login>', views.user_info),
    path('user_info/<slug:login>/<slug:post_name>', views.user_info),
    path('user_info/<slug:login>/<slug:post_name>/<int:post_number>', views.user_info),
]


