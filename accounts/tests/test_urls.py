from rest_framework.test import APITestCase
from django.urls import reverse, resolve

from .. import views


class TestURLs(APITestCase):
    def test_register_url_is_resolved(self):
        url = reverse("register")
        self.assertEqual(resolve(url).func.view_class, views.RegisterView)

    def test_login_url_is_resolved(self):
        url = reverse("login")
        self.assertEqual(resolve(url).func.view_class, views.LoginView)
