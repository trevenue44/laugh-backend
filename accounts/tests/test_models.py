from rest_framework.test import APITestCase
from faker import Faker

from .. import models


class TestLaugherModel(APITestCase):
    def setUp(self):
        self.fake = Faker()
        fake_profile = self.fake.simple_profile()
        self.data = {
            "username": fake_profile["username"],
            "password": self.fake.password(length=10),
        }

        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_creation_of_laugher(self):
        laugher = models.Laugher.objects.create_user(**self.data)
        self.assertEqual(laugher.username, self.data["username"])
        self.assertTrue(laugher.check_password(self.data["password"]))
        self.assertEqual(laugher.username, str(laugher))
        
