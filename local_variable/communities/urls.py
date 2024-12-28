from django.urls import path
from . import views

urlpatterns = [
    path('', views.community_list, name='community_list'),                # List all communities
    path('<int:community_id>/', views.community_detail, name='community_detail'),  # View a specific community
    path('create/', views.create_community, name='create_community'),     # Create a new community
    path('<int:community_id>/join/', views.join_community, name='join_community'),  # Join a community
    path('<int:community_id>/leave/', views.leave_community, name='leave_community'),  # Leave a community
]
