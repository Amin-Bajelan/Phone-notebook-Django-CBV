from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import CreateUserForm


# Create your views here.


class SignUpView(CreateView):
    form_class = CreateUserForm
    template_name = "registration/signup.html"
    success_url = "/phone_number/list-contact/"
