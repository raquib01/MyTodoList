from django.urls import path
from main import views

urlpatterns = [
    path('', views.index),
    path('add/', views.add),
    path('delete/<int:task_id>', views.delete),
    path('complete/<int:task_id>', views.complete)
]