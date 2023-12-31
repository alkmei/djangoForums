from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField


# Create your models here.
class Forum(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = AutoSlugField(populate_from="name")

    def __str__(self):
        return self.name


class Thread(models.Model):
    title = models.CharField(max_length=100)
    forums = models.ForeignKey(Forum, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from="title", unique=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    content = models.TextField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    post_id = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        if not self.id:
            last_post = (
                Post.objects.filter(thread=self.thread).order_by("-post_id").first()
            )
            self.post_id = last_post.post_id + 1 if last_post else 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Post #{self.id} in {self.thread.title}"
