from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker


class TestSetUp(APITestCase):
    def setUp(self) -> None:
        # get the endpoints for register and login
        self.register_url = reverse("register")
        self.login_url = reverse("login")

        # create a mock data for the user
        self.fake = Faker()
        fake_profile = self.fake.simple_profile()
        self.user_data = {
            "username": fake_profile["username"],
            "password": self.fake.password(length=10),
        }

        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()
