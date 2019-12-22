from django.urls import path

from shrapnel.direct_messages.views import ReceiversView, SendDirectMessageView, ReceivedDirectMessagesView, \
    SentDirectMessagesView, DirectMessageDetailView

app_name = "direct-messages"

urlpatterns = [
    path("direct-messages/receivers/", view=ReceiversView.as_view(), name="receivers"),
    path("direct-messages/send/", view=SendDirectMessageView.as_view(), name="send-direct-message"),
    path("direct-messages/received/", view=ReceivedDirectMessagesView.as_view(), name="received-direct-messages"),
    path("direct-messages/sent/", view=SentDirectMessagesView.as_view(), name="sent-direct-messages"),
    path("direct-messages/<int:direct_message_id>/", view=DirectMessageDetailView.as_view(), name="direct-message-detail"),
]
