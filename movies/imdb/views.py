from django.shortcuts import render
from .models import Movie_Post
from django.http import JsonResponse
from django.views.generic import ListView
# Create your views here.

class MovieListView(ListView):
    model = Movie_Post
    # template_name =

def movie_list(request):
    movie_list = Movie_Post.objects.all()

    data ={
        'movie':list(movie_list.values())
    }
    return JsonResponse(data)


