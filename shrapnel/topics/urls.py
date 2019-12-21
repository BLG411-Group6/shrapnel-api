from django.conf.urls import url

from shrapnel.topics.views import TopicsView, TopicDetailView

app_name = "topics"

urlpatterns = [
    url(r'^topics/$', TopicsView.as_view(), name='topics'),
    url(r'^topics/(?P<topic_id>[-\d]+)/', TopicDetailView.as_view(), name='topic-detail')
]
