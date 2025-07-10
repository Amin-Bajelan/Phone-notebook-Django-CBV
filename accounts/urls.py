from django.urls import path,include
from . import views

urlpatterns = [
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/password_change/',views.ChangePasswordView.as_view, name='change_password'),
]