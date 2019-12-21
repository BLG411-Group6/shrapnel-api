from django.urls import path

from . import views

urlpatterns = [
    path(r'register/', views.RegistrationView.as_view(), name='register'),
    path(r'login/', views.LoginView.as_view(), name='login'),
    path(r'logout/', views.LogoutView.as_view(), name='logout'),
]
