from django.urls import path
from . import views

app_name = 'problems'
urlpatterns = [
    path('probs/', views.get_probs),
    path('probs/<int:problem_id>/', views.get_prob_by_id),
    path('probs_detail/', views.get_probs_detail),
    path('create_prob/', views.create_prob),
    path('update_prob/<int:prob_id>/', views.update_prob),
    path('delete_prob/<int:prob_id>/', views.prob_delete),
]
