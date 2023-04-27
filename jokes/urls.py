from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("", view=views.JokeListView.as_view()),
    path("<int:pk>/", view=views.JokeDetailView.as_view()),
    path("user/<int:laugher_id>/", view=views.UserJokeListView.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
