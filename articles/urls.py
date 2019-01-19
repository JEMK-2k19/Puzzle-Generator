#from django.contrib import admin
from django.urls import path, re_path
from . import views

app_name = "articles"

urlpatterns = [
    #path('admin/', admin.site.urls),
    #re_path(r'^about/$', views.about),
    re_path(r'^$', views.article_list, name = "list"),
    re_path(r'^create', views.article_create, name = "create"),
    re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail")
]
