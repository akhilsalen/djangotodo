from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:todo_id>/', views.details, name='details'),
    path('create/', views.create, name='create'),
    path('details/<int:pk>/update_status/', views.update_status, name='update_status'),
]
