from django.urls import path

from shrapnel.topics.views import TopicsView, TopicDetailView, TopicEntriesView, EntriesView, EntryDetailView

app_name = "topics"

urlpatterns = [
    path("topics/", view=TopicsView.as_view(), name="topics"),
    path("topics/<int:topic_id>/", view=TopicDetailView.as_view(), name="topic-detail"),
    path("topics/<int:topic_id>/entries/", view=TopicEntriesView.as_view(), name="topic-entries"),
    path("entries/", view=EntriesView.as_view(), name="entries"),
    path("entries/<int:entry_id>/", view=EntryDetailView.as_view(), name="entry-detail")
]
