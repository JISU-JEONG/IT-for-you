from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/',views.user_signup),
    path('user/',views.user),
    path('user_delete/', views.user_delete),
    path('voice/', views.voice),
    path('users/', views.users),
    path('get_interview/<int:p_id>/', views.get_interview),
    # path('add_problem/<int:problem_pk>/', views.add_problem),
]
