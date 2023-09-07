from django.urls import path
from imdb.api.views import movie_list, each_movie_list

urlpatterns = [
    path('list/', movie_list, name = 'movie_list'),
    path('<int:pk>', each_movie_list, name = 'each_movie_list'),
]
