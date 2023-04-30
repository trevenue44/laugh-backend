from rest_framework.test import APITestCase
from faker import Faker

from .. import models
from accounts.models import Laugher


class TestJokeModel(APITestCase):
    def setUp(self) -> None:
        # data to use to create a laugher.
        # laugher needed to use it's primary key for the joke creator
        self.fake = Faker()
        fake_profile = self.fake.simple_profile()
        self.laugher_data = {
            "username": fake_profile["username"],
            "password": self.fake.password(length=10),
        }

        # create a laugher to use as the owner of jokes
        self.laugher: Laugher = Laugher.objects.create_user(**self.laugher_data)

        # data to use for the joke model
        self.joke_data = {
            "laugher": self.laugher,
            "content": "This is a fake content for testing. Laugh!",
        }

        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_creation_of_joke_without_laughed_at_by(self):
        # create joke with joke data
        joke = models.Joke.objects.create(**self.joke_data)
        # make some assertions
        self.assertEqual(joke.laugher, self.joke_data["laugher"])
        self.assertEqual(joke.content, self.joke_data["content"])

    def test_laughed_at_by_field(self):
        # create joke with data
        joke = models.Joke.objects.create(**self.joke_data)
        # setting the laughed at by field of the joke
        joke.laughed_at_by.set([self.laugher])
        # make some assertions
        self.assertTrue(joke.laughed_at_by.contains(self.laugher))
