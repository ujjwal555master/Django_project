from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='news_list'),  # List all news
    path('create/', views.create_news, name='create_news'),  # Create news (restricted to community owners)
    path('delete/<int:news_id>/', views.delete_news, name='delete_news'),
]
