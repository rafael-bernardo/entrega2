from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def lista_locais(request):
    context = {'locais': Post.objects.all()}
    return render(request, 'locais/index.html', context)


#detailview that returns 404 if not found
def detail_locais(request, pk):
    locais = get_object_or_404(Post, pk=pk)
    context = {'locais': locais}
    return render(request, 'locais/detail.html', context)
def update_locais(request, pk):
    if request.method == 'POST':
        locais = Post.objects.get(pk=pk)
        locais.title = request.POST['title']
        locais.place = request.POST['place']
        locais.content = request.POST['content']
        locais.image_url = request.POST['image_url']
        locais.save()
        return HttpResponseRedirect(reverse('locais:detail_locais', args=[locais.pk]))
    else:
        context = {'locais': Post.objects.get(pk=pk)}
        return render(request, 'locais/update.html', context)

def create_locais(request):
    if request.method == 'POST':
        locais = Post()
        locais.title = request.POST['title']
        locais.place = request.POST['place']
        locais.content = request.POST['content']
        locais.image_url = request.POST['image_url']
        locais.save()
        return HttpResponseRedirect(reverse('locais:detail_locais', args=[locais.pk]))
    else:
        return render(request, 'locais/create.html')
#delete view with confirmation page
def delete_locais(request, pk):
    if request.method == 'POST':
        locais = Post.objects.get(pk=pk)
        locais.delete()
        return HttpResponseRedirect(reverse('locais:lista_locais'))
    else:
        context = {'locais': Post.objects.get(pk=pk)}
        return render(request, 'locais/delete.html', context)
