from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('create_project', views.create_project, name='create_project'),
    path('<int:paper_id>/delete/', views.delete_project, name='delete_project'),
]