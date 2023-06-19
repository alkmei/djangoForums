from django.urls import path
from . import views

urlpatterns = [
    path("", views.forum_index, name="home"),
    path("<slug:forum_slug>", views.forum_detail, name="forum_detail"),
]
