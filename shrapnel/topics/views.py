from django.db.models import Q

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from shrapnel.topics.serializers import TopicSerializer
from shrapnel.topics.models import Topic


class TopicsView(ListCreateAPIView):
    permission_classes = []  # TODO: configure permissions.
    serializer_class = TopicSerializer

    def get_queryset(self):
        keywords = self.request.GET.get("keywords", None)
        queryset = Topic.objects.filter(is_deleted=False)

        if keywords:
            search_query = Q()
            keywords = keywords.split(",")
            for keyword in keywords:
                search_query |= Q(title__icontains=keyword.strip())

            queryset = queryset.filter(search_query)

        return queryset


class TopicDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = []  # TODO: configure permissions.
    serializer_class = TopicSerializer
    queryset = Topic.objects.filter(is_deleted=False)
    lookup_url_kwarg = 'topic_id'
    lookup_field = 'id'
