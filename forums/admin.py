from django.contrib import admin
from .models import Forum, Thread, Post


@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    exclude = ("slug",)


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    exclude = ("slug",)


admin.site.register(Post)
