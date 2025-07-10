from django.views.generic.edit import CreateView
from .forms import CreateUserForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import logout
from django.shortcuts import redirect


# Create your views here.


class SignUpView(CreateView):
    """
    class SignUp for create new user
    """
    form_class = CreateUserForm
    template_name = "registration/signup.html"
    success_url = "/accounts/login/"


class ChangePasswordView(PasswordChangeView):
    """
    class ChangePassword for change password of user and redirect to login page
    """
    def form_valid(self, form):
        response = super().form_valid(form)
        logout(self.request)
        return redirect('/accounts/login/')