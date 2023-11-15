from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import PostForm
# Create your views here.

def lista_locais(request):
    context = {'locais': Post.objects.all()}
    return render(request, 'locais/index.html', context)


def detail_locais(request, pk):
    locais = get_object_or_404(Post, pk=pk)
    context = {'locais': locais}
    return render(request, 'locais/detail.html', context)

def update_locais(request, pk):
    locais = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        forms = PostForm(request.POST, instance=locais)
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect(reverse('locais:lista_locais'))
    forms = PostForm(instance=locais)
    context = {'form': forms}
    return render(request, 'locais/update.html', context)

def create_locais(request):
    if request.method == 'POST':
        forms = PostForm(request.POST)
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect(reverse('locais:lista_locais'))
    forms = PostForm()
    context = {'form': forms}
    return render(request, 'locais/create.html', context)

#delete view with confirmation page
def delete_locais(request, pk):
    if request.method == 'POST':
        locais = Post.objects.get(pk=pk)
        locais.delete()
        return HttpResponseRedirect(reverse('locais:lista_locais'))
    else:
        context = {'locais': Post.objects.get(pk=pk)}
        return render(request, 'locais/delete.html', context)
