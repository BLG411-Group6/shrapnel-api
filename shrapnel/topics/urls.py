from django.conf.urls import url

from shrapnel.topics.views import TopicsView

app_name = "topics"

urlpatterns = [
    url(r'^topics/$', TopicsView.as_view(), name='topics'),
]
