from django.urls import path
from . import views

urlpatterns = [
    path('quiz/', views.quiz_view, name='quiz'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard')
]