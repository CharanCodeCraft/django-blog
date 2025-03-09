from django import forms
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Post
class createBlog(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']