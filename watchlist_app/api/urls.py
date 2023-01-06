from watchlist_app.api.views import movie_list, movie_details
from django.urls import path

urlpatterns = [
    path('allmovies/', movie_list, name='movie list'),
    path('movie/<int:pk>', movie_details, name='movie details')
]
