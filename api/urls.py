from django.urls import path, include
from . import views

urlpatterns = [
    path("", view=views.HomeView.as_view(), name="home"),
    path("accounts/", include("accounts.urls")),
]
