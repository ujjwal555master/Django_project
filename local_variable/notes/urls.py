from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.note_list, name='note_list'),           # List all notes
    path('<int:pk>/', views.note_detail, name='note_detail'),  # View a single note
    path('add/', views.add_note, name='add_note'),         # Add a new note
    path('<int:pk>/edit/', views.edit_note, name='edit_note'), # Edit a note
    path('<int:pk>/delete/', views.delete_note, name='delete_note'), # Delete a note
]
