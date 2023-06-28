from django import forms

from forums.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["content"]
