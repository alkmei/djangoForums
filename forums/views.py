from django.shortcuts import render, get_object_or_404, redirect
from .models import Forum, Thread, Post
from .forms import PostForm, ThreadForm
from django.contrib.auth.decorators import login_required


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


@login_required
def forum_create(request, forum_slug):
    if request.method == "POST":
        form = ThreadForm(request.POST)
        if form.is_valid():
            forum = get_object_or_404(Forum, slug=forum_slug)
            thread = form.save(commit=False)
            thread.creator = request.user
            thread.forums = forum
            thread.save()

            content = form.cleaned_data["content"]
            Post.objects.create(thread=thread, content=content, creator=request.user)

            return redirect("forum_detail", forum_slug)
    else:
        form = ThreadForm()
    return render(request, "forums/create_thread.html", {"form": form})
