from .models import Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'place', 'content', 'image_url']
    title = forms.CharField(max_length=100, required=True)
    place = forms.CharField(max_length=100, required=True)
    content = forms.CharField(required=True)
    image_url = forms.CharField(required=False)