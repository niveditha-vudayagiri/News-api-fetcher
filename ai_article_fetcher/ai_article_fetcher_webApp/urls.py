from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("disp_news/", views.disp_news, name="disp_news")
]