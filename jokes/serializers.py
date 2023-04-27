from rest_framework import serializers

from . import models


class JokeListSerializer(serializers.ModelSerializer):
    num_laughs = serializers.ReadOnlyField(source="laughed_at_by.count")
    laugher_name = serializers.ReadOnlyField(source="laugher.username")

    class Meta:
        model = models.Joke
        fields = (
            "id",
            "content",
            "laugher",
            "laugher_name",
            "laughed_at_by",
            "num_laughs",
            "date_published",
        )


class JokeCreateSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    laugher_name = serializers.ReadOnlyField(source="laugher.username")
    laughed_at_by = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    num_laughs = serializers.ReadOnlyField(source="laughed_at_by.count")
    date_published = serializers.ReadOnlyField()

    class Meta:
        model = models.Joke
        fields = (
            "id",
            "content",
            "laugher",
            "laugher_name",
            "laughed_at_by",
            "num_laughs",
            "date_published",
        )


class JokeUpdateSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    laugher = serializers.PrimaryKeyRelatedField(read_only=True)
    laugher_name = serializers.ReadOnlyField(source="laugher.username")
    num_laughs = serializers.ReadOnlyField(source="laughed_at_by.count")
    date_published = serializers.ReadOnlyField()

    class Meta:
        model = models.Joke
        fields = (
            "id",
            "content",
            "laugher",
            "laugher_name",
            "laughed_at_by",
            "num_laughs",
            "date_published",
        )
