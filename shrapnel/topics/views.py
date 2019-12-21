from django.db.models import Q

from rest_framework.generics import ListCreateAPIView

from shrapnel.topics.serializers import TopicSerializer
from shrapnel.topics.models import Topic


class TopicsView(ListCreateAPIView):
    permission_classes = []
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
