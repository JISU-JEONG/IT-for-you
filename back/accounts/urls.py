from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/',views.user_signup),
    path('user/',views.user),
    path('user_delete/', views.user_delete),
]
