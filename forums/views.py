from django.shortcuts import render, get_object_or_404
from .models import Forum, Thread


def forum_index(request):
    forums = Forum.objects.all()
    context = {"forums": forums}
    return render(request, "home.html", context)


def forum_detail(request, forum_slug):
    forum = get_object_or_404(Forum, slug=forum_slug)
    threads = forum.thread_set.all()
    context = {"threads": threads}
    return render(request, "forum.html", context)
