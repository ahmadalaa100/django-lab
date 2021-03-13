from django.shortcuts import render,redirect
from .forms import movieForm

# Create your views here.
def index(request):
    movies = movie.object.all()

    return render(request,'netfilx/index.html',{
        "movies" : movies
    })


def show(request,id):
    movie = movie.object.get(PK=id)
    return render(request,'netfilx/show.html',{
        "movie" : movie
    })

def create(request):
    form = movieForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request,'netfilx/create.html',{
        "form" : form
    })



def update(request):
    movie = movie.object.get(PK=id)
    form = movieForm(request.POST or None , request.FILES or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request,'netfilx/edit.html',{
        "form" : form,
        "movie" : movie
    })

def delete(request,id):
    movie = movie.object.get(PK=id)
    movie.delete()
    return redirect('index')