from django.shortcuts import render, get_object_or_404, redirect
from .models import Forum, Thread
from .forms import PostForm


def forum_index(request):
    forums = Forum.objects.all()
    context = {"forums": forums}
    return render(request, "home.html", context)


def forum_detail(request, forum_slug):
    forum = get_object_or_404(Forum, slug=forum_slug)
    threads = forum.thread_set.all()
    context = {"threads": threads, "forum": forum}
    return render(request, "forums/forum.html", context)


def thread_detail(request, forum_slug, thread_slug):
    thread = get_object_or_404(Thread, slug=thread_slug, forums__slug=forum_slug)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.creator = request.user
            post.save()
            return redirect("thread_detail", forum_slug, thread_slug)

    else:
        form = PostForm()

    posts = thread.post_set.all()
    context = {"thread": thread, "posts": posts, "form": form}
    return render(request, "forums/thread.html", context)
