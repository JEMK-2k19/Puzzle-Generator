from django.urls import path, re_path
from . import views

app_name = "carpark"

urlpatterns = [
    re_path(r'^$', views.carpark_view, name="carpark_view"),
    re_path(r'^quiz', views.quiz, name="quiz")
]