from rest_framework.generics import ListCreateAPIView

from shrapnel.topics.serializers import TopicSerializer
from shrapnel.topics.models import Topic


class TopicsView(ListCreateAPIView):
    permission_classes = []
    serializer_class = TopicSerializer
    queryset = Topic.objects.filter(is_deleted=False)
