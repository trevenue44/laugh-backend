from django.db import models

from accounts.models import Laugher


# Create your models here.
class Joke(models.Model):
    # the person who published the joke
    laugher = models.ForeignKey(Laugher, on_delete=models.CASCADE)

    # the content of the joke
    content = models.CharField(max_length=125)
    date_published = models.DateTimeField(auto_now_add=True, blank=True)
    # the laughers who laughed at the joke. Number of laughs
    laughs = models.ManyToManyField(Laugher, blank=True, related_name="laughs")

    def __str__(self) -> str:
        return self.content
