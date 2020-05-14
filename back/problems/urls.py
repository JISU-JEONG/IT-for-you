from django.urls import path
from . import views

app_name = 'problems'
urlpatterns = [
    path('get_prob/', views.get_prob)
]
