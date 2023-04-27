from rest_framework import serializers

from . import models


class JokeListSerializer(serializers.ModelSerializer):
    num_laughs = serializers.ReadOnlyField(source="laughs.count")
    laugher = serializers.ReadOnlyField(source="laugher.username")

    class Meta:
        model = models.Joke
        fields = ("id", "content", "laugher", "num_laughs", "laughs", "date_published")


class JokeCreateSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    laugher = serializers.ReadOnlyField(source="laugher.username")
    num_laughs = serializers.ReadOnlyField(source="laughs.count")
    laughs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    date_published = serializers.ReadOnlyField()

    class Meta:
        model = models.Joke
        fields = ("id", "content", "laugher", "num_laughs", "laughs", "date_published")


class JokeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Joke
        fields = ("content", "laughs")
