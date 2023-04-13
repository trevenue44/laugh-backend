from django.urls import path
from . import views

urlpatterns = [
    path("register/", view=views.RegisterView.as_view(), name="register"),
    path("login/", view=views.LoginView.as_view(), name="login"),
]
