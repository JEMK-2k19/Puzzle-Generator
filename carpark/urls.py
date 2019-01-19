from django.urls import path, re_path
from . import views

app_name = "carpark"

urlpatterns = [
    re_path(r'^', views.new_view, name="new_view"),
    re_path(r'^new_game/', views.new_game, name="new_game"),
    re_path(r'^join_game/', views.join_game, name="join_game"),
    re_path(r'^quiz/', views.quiz, name="quiz")
]