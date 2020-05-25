from django.urls import path
from . import views

app_name = 'problems'
urlpatterns = [
    path('prob_cate/', views.get_prob_cate),
    path('prob_type/', views.get_prob_type),
    path('prob_diff/', views.get_prob_diff),
    path('probs/', views.get_probs),
    path('probs/<int:problem_id>/', views.get_prob_by_id),
    path('probs_detail/', views.get_probs_detail),
    path('create_prob/', views.create_prob),
    path('update_prob/<int:prob_id>/', views.update_prob),
    path('delete_prob/<int:prob_id>/', views.prob_delete),
    path('x_note/<int:user_id>/', views.x_note),
    path('x_note_add/', views.x_note_add),
]
