from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from shrapnel.topics.serializers import TopicSerializer, EntrySerializer, SimpleEntrySerializer
from shrapnel.topics.models import Topic, Entry
from shrapnel.core.utils import TopicResourceMixin, filter_queryset_by_keywords


class TopicsView(ListCreateAPIView):
    permission_classes = []  # TODO: configure permissions.
    serializer_class = TopicSerializer

    def get_queryset(self):
        return filter_queryset_by_keywords(request=self.request, queryset=Topic.objects.filter(is_deleted=False), field="title")


class TopicDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = []  # TODO: configure permissions.
    serializer_class = TopicSerializer
    queryset = Topic.objects.filter(is_deleted=False)
    lookup_url_kwarg = 'topic_id'
    lookup_field = 'id'


class TopicEntriesView(TopicResourceMixin, ListCreateAPIView):
    permission_classes = []  # TODO: configure permissions.
    serializer_class = SimpleEntrySerializer

    def get_queryset(self):
        return filter_queryset_by_keywords(request=self.request, queryset=Entry.objects.filter(is_deleted=False), field="content")


class EntriesView(ListAPIView):
    permission_classes = []  # TODO: configure permissions.
    serializer_class = EntrySerializer

    def get_queryset(self):
        return filter_queryset_by_keywords(request=self.request, queryset=Entry.objects.filter(is_deleted=False), field="content")


class EntryDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = []  # TODO: configure permissions.
    serializer_class = EntrySerializer
    queryset = Entry.objects.filter(is_deleted=False)
    lookup_url_kwarg = 'entry_id'
    lookup_field = 'id'
