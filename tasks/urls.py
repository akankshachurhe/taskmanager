from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_task, name='create_task'),
    path('complete/<int:task_id/', views.complete_task, name='complete_task'),
    path('accounts/login/', views.login, name='login'),
]

