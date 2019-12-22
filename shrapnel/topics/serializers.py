from drf_extra_fields.relations import PresentablePrimaryKeyRelatedField

from rest_framework import serializers

from shrapnel.topics.models import Topic, Entry
from shrapnel.users.serializers import UserSerializer


class SimpleEntrySerializer(serializers.ModelSerializer):
    user = PresentablePrimaryKeyRelatedField(presentation_serializer=UserSerializer, read_only=True)

    class Meta:
        model = Entry
        fields = [
            "id",
            "content",
            "user",
            "date_created",
            "date_updated"
        ]
        read_only_fields = ["date_created", "date_updated"]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        validated_data["topic"] = self.context["topic"]
        return super(SimpleEntrySerializer, self).create(validated_data)


class TopicSerializer(serializers.ModelSerializer):
    user = PresentablePrimaryKeyRelatedField(presentation_serializer=UserSerializer, read_only=True)
    entries = PresentablePrimaryKeyRelatedField(presentation_serializer=SimpleEntrySerializer, many=True, read_only=True)

    class Meta:
        model = Topic
        fields = [
            "id",
            "title",
            "user",
            "entries",
            "date_created",
            "date_updated",
        ]
        read_only_fields = ["date_created", "date_updated"]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super(TopicSerializer, self).create(validated_data)


class SimpleTopicSerializer(serializers.ModelSerializer):
    user = PresentablePrimaryKeyRelatedField(presentation_serializer=UserSerializer, read_only=True)

    class Meta:
        model = Topic
        fields = [
            "id",
            "title",
            "user",
            "date_created",
            "date_updated",
        ]
        read_only_fields = ["date_created", "date_updated"]


class EntrySerializer(serializers.ModelSerializer):
    topic = PresentablePrimaryKeyRelatedField(presentation_serializer=SimpleTopicSerializer, read_only=True)
    user = PresentablePrimaryKeyRelatedField(presentation_serializer=UserSerializer, read_only=True)

    class Meta:
        model = Entry
        fields = [
            "id",
            "content",
            "user",
            "topic",
            "date_created",
            "date_updated"
        ]
        read_only_fields = ["date_created", "date_updated", "topic"]
