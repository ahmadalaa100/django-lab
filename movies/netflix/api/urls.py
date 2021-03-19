from django.urls import path,include
from .views import index,create,movieList,createMovie,updateMovie,api_signup
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
  
  path("login/", obtain_auth_token),
  path("signup",api_signup),
  path("",index),
  path("create",create),
  path("list/",movieList.as_view()),
  path("store/",createMovie.as_view()),
  path("store/<int:pk>",updateMovie.as_view())
]