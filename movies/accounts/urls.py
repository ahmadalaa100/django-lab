from django.urls import path,include
from . import views


rlpatterns = [
    
    path('signup',views.signup ,name="signup")
   
]