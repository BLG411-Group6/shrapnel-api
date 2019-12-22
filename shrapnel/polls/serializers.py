from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from ..users.serializers import SimpleUserSerializer
from .models import Poll, PollOption, PollAnswer


class PollOptionSerializer(serializers.ModelSerializer):
    number_of_answers = serializers.SerializerMethodField()

    class Meta:
        model = PollOption
        fields = [
            'id',
            'body',
            'number_of_answers',
            'date_created'
        ]
        read_only_fields = ['date_created']

    def get_number_of_answers(self, poll_option):
        return PollAnswer.objects.filter(option=poll_option).count()

    def create(self, validated_data):
        if validated_data.get('poll') is None:
            validated_data['poll'] = self.context.get('poll')
        return super().create(validated_data)


class PollSerializer(WritableNestedModelSerializer):
    user = SimpleUserSerializer(read_only=True)
    options = PollOptionSerializer(many=True)

    class Meta:
        model = Poll
        fields = [
            'id',
            'title',
            'user',
            'options',
            'date_created',
            'date_expiration'
        ]
        read_only_fields = ['date_created']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class PollAnswerSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer(read_only=True)
    poll = PollSerializer(read_only=True)
    option = PollOptionSerializer(read_only=True)

    class Meta:
        model = PollAnswer
        fields = [
            'id',
            'user',
            'poll',
            'option',
            'date_created',
            'date_updated',
        ]
        read_only_fields = ['date_created', 'date_updated']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        validated_data['poll'] = self.context['poll']
        validated_data['option'] = self.context['option']
        return super().create(validated_data)
