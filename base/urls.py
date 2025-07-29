from . import views 
from django.urls import path,include


urlpatterns = [
    path('', views.home , name="home"),
    path('post/<str:pk>/', views.post , name="post"),
    path('send_email/', views.sendEmail, name="send_email"),
]