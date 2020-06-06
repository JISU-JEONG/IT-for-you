from django.urls import path
from . import views

app_name = 'interprobs'
urlpatterns = [
    path('search/', views.InterSearch.as_view()),
    # path('interviews/',views.ViewInterviews),
    path('voice/', views.voice),
    # path('get_interview/<int:p_id>/', views.get_interview),
    # path('get_audio/<int:p_id>/', views.get_audio),
    path('myinters/<int:user_id>/', views.MyInterview.as_view()),
    path('myinters/<int:user_id>/<int:myinter_id>/', views.MyInterviewDetail.as_view()),
]