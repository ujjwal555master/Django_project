from django.urls import path
from . import views

urlpatterns = [
    path('', views.paper_list, name='paper_list'),                # List all question papers
    path('upload/', views.upload_paper, name='upload_paper'),      # Upload a new question paper
    path('<int:paper_id>/', views.paper_detail, name='paper_detail'),  # View a single question paper
    path('<int:paper_id>/delete/', views.delete_paper, name='delete_paper'),  # Delete a question paper
]
