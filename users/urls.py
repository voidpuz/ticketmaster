from django.urls import path

from users.template_views import *


urlpatterns = [
    path('login/', LoginView.as_view(), name="login-template"),
    path('register/', RegisterView.as_view(), name="register-template"),
    path('profile/<int:pk>/', ProfileView.as_view(), name="profile-template"),
]
