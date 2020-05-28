from django.urls import path
from . import views

app_name = 'xnotes'
urlpatterns = [
    path('mynote/<int:user_id>/', views.MyNote.as_view()),
    path('mynote/<int:user_id>/<int:note_id>/', views.MyNoteDetail.as_view()),
]
