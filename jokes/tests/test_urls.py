from rest_framework.test import APITestCase
from django.urls import resolve, reverse

from .. import views


class TestURLs(APITestCase):
    """
    Test case to make sure that the right views are rendered when\
    enpoints are hit.
    """

    def test_joke_list_create_url_is_resolved(self):
        url = reverse("joke_list_create")
        # making sure the right view is rendered when the endpoint is hit.
        self.assertEqual(resolve(url).func.view_class, views.JokeListView)

    def test_joke_detail_url_is_resolved(self):
        url = reverse("joke_detail", kwargs={"pk": 1})
        # making sure the right view is rendered when the endpoint is hit
        self.assertEqual(resolve(url).func.view_class, views.JokeDetailView)

    def test_specific_user_jokes_url_is_resolved(self):
        url = reverse("specific_user_jokes", kwargs={"laugher_id": 1})
        self.assertEqual(resolve(url).func.view_class, views.UserJokeListView)
