from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import signupForm

# Create your views here.

class signup_user(CreateView):
    form_class = signupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')