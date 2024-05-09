"""
URL configuration for DjangorestProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.movie_app_director_list_api_view),
    path('api/v1/directors/<int:id>/', views.movie_app_director_detail_api_view),
    path('api/v1/movies/', views.movie_app_movie_list_api_view),
    path('api/v1/movies/<int:id>/', views.movie_app_movie_detail_api_view),
    path('api/v1/reviews/', views.movie_app_review_list_api_view),
    path('api/v1/reviews/<int:id>/', views.movie_app_review_detail_api_view),

]
