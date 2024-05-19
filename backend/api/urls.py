from django.urls import path
from . import views

urlspatterns = [
  path("notes/", views.NoteListCreate.as_view(), name="note-list"),
  path("nates/delete/<int:pk>", views.NoteDelete.as_view(), name="delete-note"),
  
]