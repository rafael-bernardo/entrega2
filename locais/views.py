from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
# Create your views here.

class LocaisList(ListView):
    model = Post
    template_name = 'locais/index.html'
    context_object_name = 'locais'

class LocaisDetail(DetailView):
    model = Post
    template_name = 'locais/detail.html'
    context_object_name = 'locais'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object).order_by('-created_at')
        return context
    
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

def comment_create(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('locais:detail_locais', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'locais/comment_create.html', {'form': form})