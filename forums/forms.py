from django import forms

from forums.models import Post, Thread


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["content"]


class ThreadForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Thread
        fields = ["title", "content"]
