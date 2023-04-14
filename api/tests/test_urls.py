from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse, resolve

from .. import views


class TestURLs(APITestCase):
    def test_api_home_route(self) -> None:
        home_url = reverse("home")
        response = self.client.get(home_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # making sure that it's the whoel view that's linked to home endpoint
        self.assertEqual(resolve(home_url).func.view_class, views.HomeView)
