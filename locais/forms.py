from .models import Post, Comment
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'place', 'categories',  'content', 'image_url']
    title = forms.CharField(max_length=100, required=True)
    place = forms.CharField(max_length=100, required=True)
    content = forms.CharField(required=True)
    image_url = forms.CharField(required=False)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']
    content = forms.CharField(required=True)
    