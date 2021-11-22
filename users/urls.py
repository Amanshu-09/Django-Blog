from django.urls import path,include
from .views import *

urlpatterns = [
    path('signup', signup_user.as_view(), name='signup'),
]