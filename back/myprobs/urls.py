from django.urls import path
from . import views

app_name = 'myprobs'
urlpatterns = [
    path('myprob/<int:user_id>/', views.MyProblem.as_view()),
    path('myprob/<int:user_id>/<int:myprob_id>/', views.MyProblemDetail.as_view()),
]
