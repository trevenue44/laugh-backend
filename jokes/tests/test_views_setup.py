from rest_framework.test import APITestCase
from django.urls import reverse

from accounts.models import Laugher
from jokes.models import Joke


class TestViewsSetup(APITestCase):
    def setUp(self) -> None:
        # create two Laughers
        self.laugher1 = Laugher.objects.create_user(
            username="laugher1", password="laugher1"
        )
        self.laugher2 = Laugher.objects.create_user(
            username="laugher2", password="laugher2"
        )

        # create two jokes
        self.joke1 = Joke.objects.create(
            laugher=self.laugher1, content="This is a joke"
        )
        self.joke2 = Joke.objects.create(
            laugher=self.laugher2, content="This is another joke"
        )

        # create urls
        self.joke_list_create_url = reverse("joke_list_create")
        self.joke_detail_url = reverse("joke_detail", kwargs={"pk": self.joke1.id})
        self.specific_user_jokes_url = reverse(
            "specific_user_jokes", kwargs={"laugher_id": self.laugher1.id}
        )

        # create some constants
        self.laugher1_jokes_count = len(self.laugher1.jokes.all())

        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()
