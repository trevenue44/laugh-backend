from .test_views_setup import TestViewsSetup
from rest_framework import status


class TestViews(TestViewsSetup):
    def test_joke_list_create_view(self):
        response = self.client.get(self.joke_list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_joke_view(self):
        create_joke_data = {"laugher": self.laugher1.id, "content": "This is a joke"}
        response = self.client.post(
            self.joke_list_create_url,
            create_joke_data,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["laugher"], self.laugher1.id)
        self.assertEqual(response.data["content"], create_joke_data["content"])
        # make sure the joke was created
        self.assertEqual(len(self.laugher1.jokes.all()), self.laugher1_jokes_count + 1)
        # making sure the joke gets added to the queryset of jokes when the endpoint is hit
        get_response = self.client.get(self.joke_list_create_url)
        self.assertEqual(len(get_response.data), 3)

    def test_joke_detail_view(self):
        response = self.client.get(self.joke_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["laugher"], self.joke1.laugher.id)
        self.assertEqual(response.data["content"], self.joke1.content)

    def test_specific_user_jokes_view(self):
        response = self.client.get(self.specific_user_jokes_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["laugher"], self.laugher1.id)
        self.assertEqual(response.data[0]["content"], self.joke1.content)

    def test_update_joke_view(self):
        update_joke_data = {"content": "This is an updated joke"}
        response = self.client.put(
            self.joke_detail_url,
            update_joke_data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["laugher"], self.joke1.laugher.id)
        self.assertEqual(response.data["content"], update_joke_data["content"])
