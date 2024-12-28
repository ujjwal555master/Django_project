from django.urls import path
from . import views

urlpatterns = [
    path('message/<int:id>/', views.message_detail, name='message_detail'),

    path('inbox/', views.inbox, name='inbox'),  # View received messages
    path('send/', views.send_message, name='send_message'),  # Send a messages
    path('', views.profile),
    path('login/', views.user_login, name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('logout/', views.log_out, name='logout'),
    path('<str:username>/', views.profile_view, name='profile_view'),  # View profile
    path('<str:username>/edit/', views.edit_profile, name='edit_profile'),  # Edit profile
    path('profile/<int:user_id>/', views.user_profile, name='user_profile'),
]