from rest_framework import generics

from . import models, serializers


class JokeListView(generics.ListCreateAPIView):
    """
    GET: Retrieve all jokes in the DB.
    POST: Create a new joke with content and laugher id provided in the body of request
    """

    queryset = models.Joke.objects.all()
    serializer_class = serializers.JokeListSerializer

    # custom function to choose appropriate serializer class based on
    # whether a joke is being added or jokes are being displayed.
    def get_serializer_class(self):
        if self.request.method == "POST":
            return serializers.JokeCreateSerializer
        return super().get_serializer_class()


class UserJokeListView(generics.ListAPIView):
    """
    GET: returns all the jokes of the provided laugher's ID
    """

    serializer_class = serializers.JokeListSerializer

    # using a custom function to get queryset that contains only
    # jokes from a specified user
    def get_queryset(self):
        return models.Joke.objects.filter(laugher_id=self.kwargs["laugher_id"])


class JokeDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: returns the details of a specified joke ID.
    DELETE: deletes the joke with the specified joke ID.
    PUT: updates the details of a joke
    """

    queryset = models.Joke.objects.all()
    serializer_class = serializers.JokeListSerializer

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return serializers.JokeUpdateSerializer
        return super().get_serializer_class()
