from django.urls import path
from . import views

urlpatterns = [
    path("register/", view=views.RegisterView.as_view(), name="accounts-register")
]