from django.urls import path
from . import views

urlpatterns = [
    path("", views.forum_index, name="home"),
    path("<slug:forum_slug>", views.forum_detail, name="forum_detail"),
    path("<slug:forum_slug>/create", views.forum_create, name="forum_create"),
    path(
        "<slug:forum_slug>/<slug:thread_slug>",
        views.thread_detail,
        name="thread_detail",
    ),
]
