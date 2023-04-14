from .test_setup import TestSetUp
from rest_framework import status


class TestViews(TestSetUp):
    def test_user_cannot_register_without_data(self):
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_cannot_register_with_password_less_than_8_characters(self):
        user_data_short_password = self.user_data.copy()
        user_data_short_password["password"] = self.fake.password(length=7)
        response = self.client.post(
            self.register_url, user_data_short_password, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_can_register(self):
        response = self.client.post(self.register_url, self.user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["username"], self.user_data["username"])
