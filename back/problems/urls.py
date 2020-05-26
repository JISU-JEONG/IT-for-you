from django.urls import path
from . import views

app_name = 'problems'
urlpatterns = [
    path('prob_cate/', views.get_prob_cate),
    path('prob_type/', views.get_prob_type),
    path('prob_diff/', views.get_prob_diff),
    path('probs/', views.Prob.as_view()),
    path('probs/<int:problem_id>/', views.SpecProb.as_view()),
]
