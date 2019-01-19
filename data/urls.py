#from django.contrib import admin
from django.urls import path, re_path
from . import views

app_name = "data"

urlpatterns = [
    re_path(r'^data_input', views.csv_input, name = 'input'),
    re_path(r'^csv', views.csv_view, name = "csv"),
    re_path(r'^js_test', views.js_test, name = 'js'),
    re_path(r'^analyse_text', views.text_analyse, name = 'text'),
    re_path(r'^text_output', views.text_csv, name = 'text_output'),
    re_path(r'^transliterate', views.transliterate, name = 'transliterate'),
    re_path(r'^transliterate_output', views.transliterate_output, name = 'transliterate_output'),
    re_path(r'^random_sents', views.random_sents, name = 'random_sents'),
    re_path(r'^random_output', views.random_output, name = 'random_output')
]
