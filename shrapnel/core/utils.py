from django.utils.functional import cached_property
from django.shortcuts import get_object_or_404
from django.db.models import Q

from shrapnel.topics.models import Topic


class TopicResourceMixin(object):
    topic_queryset = Topic.objects.filter(is_deleted=False)
    topic_lookup_url_kwarg = 'topic_id'
    topic_lookup_field = 'id'

    @cached_property
    def topic(self):
        return get_object_or_404(
            self.topic_queryset,
            **{self.topic_lookup_field: self.kwargs[self.topic_lookup_url_kwarg]}
        )

    def get_serializer_context(self):
        serializer_context = super(TopicResourceMixin, self).get_serializer_context()
        serializer_context["topic"] = self.topic
        return serializer_context


def filter_queryset_by_keywords(request, queryset, field):
    keywords = request.GET.get("keywords", None)

    if keywords:
        search_query = Q()
        keywords = keywords.split(",")
        for keyword in keywords:
            search_query |= Q(**{field + "__icontains": keyword.strip()})

        queryset = queryset.filter(search_query)

    return queryset
