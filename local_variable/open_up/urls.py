from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),           # List all posts
    path('create/', views.create_post, name='create_post'),  # Create a new post
    path('<int:post_id>/', views.post_detail, name='post_detail'),  # View a single post
    path('<int:post_id>/edit/', views.edit_post, name='edit_post'),  # Edit a post
    path('<int:post_id>/delete/', views.delete_post, name='delete_post'),  # Delete a post
]
