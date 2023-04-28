from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("", view=views.JokeListView.as_view(), name="joke_list_create"),
    path("<int:pk>/", view=views.JokeDetailView.as_view(), name="joke_detail"),
    path(
        "user/<int:laugher_id>/",
        view=views.UserJokeListView.as_view(),
        name="specific_user_jokes",
    ),
]


urlpatterns = format_suffix_patterns(urlpatterns)
