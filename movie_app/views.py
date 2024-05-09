from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Director, Movie, Review
from .serializers import (DirectorSerializer, MovieSerializer, ReviewSerializer,
                          DirectorDetailSerializer, MovieDetailSerializer, ReviewDetailSerializer)

@api_view(['GET'])
def movie_app_director_list_api_view(request):
    directors = Director.objects.all()
    list1 = DirectorSerializer(directors, many=True).data
    return Response(data=list1)

@api_view(['GET'])
def movie_app_director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director Not Found'},
                        status=status.HTTP_404_NOT_FOUND)

    data1 = DirectorDetailSerializer(director, many=False).data
    return Response(data=data1)

@api_view(['GET'])
def movie_app_movie_list_api_view(request):
    movies = Movie.objects.all()
    list2 = MovieSerializer(movies, many=True).data
    return Response(data=list2)

@api_view(['GET'])
def movie_app_movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie Not Found'},
                        status=status.HTTP_404_NOT_FOUND)

    data2 = MovieDetailSerializer(movie, many=False).data
    return Response(data=data2)

@api_view(['GET'])
def movie_app_review_list_api_view(request):
    reviews = Review.objects.all()
    list3 = ReviewSerializer(reviews, many=True).data
    return Response(data=list3)

@api_view(['GET'])
def movie_app_review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review Not Found'},
                        status=status.HTTP_404_NOT_FOUND)

    data3 = ReviewDetailSerializer(review, many=False).data
    return Response(data=data3)


