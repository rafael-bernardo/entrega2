from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import PostForm
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.detail import DetailView

# Create your views here.

class LocaisList(ListView):
    model = Post
    template_name = 'locais/index.html'
    context_object_name = 'locais'

class LocaisDetail(DetailView):
    model = Post
    template_name = 'locais/detail.html'
    context_object_name = 'locais'

class LocaisCreate(CreateView):
    model = Post
    template_name = 'locais/create.html'
    form_class = PostForm
    success_url = '/locais'

class LocaisUpdate(UpdateView):
    model = Post
    template_name = 'locais/update.html'
    form_class = PostForm
    success_url = '/locais'

class LocaisDelete(DeleteView):
    model = Post
    template_name = 'locais/delete.html'
    success_url = '/locais'
    context_object_name = 'locais'
