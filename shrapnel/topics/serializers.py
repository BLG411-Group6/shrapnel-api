from drf_extra_fields.relations import PresentablePrimaryKeyRelatedField

from rest_framework import serializers

from shrapnel.topics.models import Topic
from shrapnel.users.models import User
from shrapnel.topics.models import Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = [
            "id",
            "content",
            "topic",
            "user",
            "date_created",
            "date_updated"
        ]
        read_only_fields = ["date_created", "date_updated"]


class TopicSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(is_deleted=False), required=True)
    entries = PresentablePrimaryKeyRelatedField(presentation_serializer=EntrySerializer, many=True, read_only=True)

    class Meta:
        model = Topic
        fields = [
            "id",
            "title",
            "user",
            "entries"
            "date_created",
            "date_updated",
        ]
        read_only_fields = ["date_created", "date_updated"]

    # TODO: Set user to request.user while creating and make user field read only.
