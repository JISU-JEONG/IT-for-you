from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/',views.user_signup),
    path('user/',views.user),
    path('user_delete/<int:user_id>/', views.user_delete),
    path('users/', views.users),
    path('userprob/', views.SaveProb.as_view()),
]
