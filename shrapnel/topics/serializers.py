from rest_framework import serializers

from shrapnel.topics.models import Topic
from shrapnel.users.models import User


class TopicSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(is_deleted=False), required=True)

    class Meta:
        model = Topic
        fields = (
            "title",
            "user",
            "date_created",
            "date_updated"
        )

    # TODO: Set user to request.user and make user field read only.
