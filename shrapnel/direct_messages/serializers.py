from drf_extra_fields.relations import PresentablePrimaryKeyRelatedField

from rest_framework import serializers
from rest_framework.validators import ValidationError

from shrapnel.direct_messages.models import DirectMessage
from shrapnel.users.models import User
from shrapnel.users.serializers import SimpleUserSerializer


class DirectMessageSerializer(serializers.ModelSerializer):
    sender = PresentablePrimaryKeyRelatedField(presentation_serializer=SimpleUserSerializer, read_only=True)
    receiver = PresentablePrimaryKeyRelatedField(presentation_serializer=SimpleUserSerializer, queryset=User.objects.filter(is_deleted=False))

    class Meta:
        model = DirectMessage
        fields = [
            "id",
            "title",
            "content",
            "sender",
            "receiver",
            "is_read",
            "date_created"
        ]
        read_only_fields = ["is_read", "date_created"]

    def validate_receiver(self, receiver):
        if receiver == self.context["request"].user:
            raise ValidationError("You cannot send direct message to yourself.")

        return receiver

    def create(self, validated_data):
        validated_data["sender"] = self.context["request"].user
        return super(DirectMessageSerializer, self).create(validated_data)
