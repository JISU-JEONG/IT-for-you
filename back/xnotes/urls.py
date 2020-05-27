from django.urls import path
from . import views

app_name = 'xnotes'
urlpatterns = [
    path('mynote/', views.MyNote.as_view()),
    path('mynote/<int:note_id>', views.MyNoteDetail.as_view()),
]
