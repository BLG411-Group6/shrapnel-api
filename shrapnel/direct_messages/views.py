from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from shrapnel.direct_messages.models import DirectMessage
from shrapnel.direct_messages.serializers import DirectMessageSerializer
from shrapnel.users.models import User
from shrapnel.users.serializers import SimpleUserSerializer
from shrapnel.core.permissions import IsReceiverOrSender


class ReceiversView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SimpleUserSerializer

    def get_queryset(self):
        return User.objects.filter(is_deleted=False).exclude(id=self.request.user.id)


class SendDirectMessageView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DirectMessageSerializer


class ReceivedDirectMessagesView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DirectMessageSerializer

    def get_queryset(self):
        return DirectMessage.objects.filter(receiver=self.request.user.id, is_deleted_by_receiver=False)


class SentDirectMessagesView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DirectMessageSerializer

    def get_queryset(self):
        return DirectMessage.objects.filter(sender=self.request.user.id, is_deleted_by_sender=False)


class DirectMessageDetailView(RetrieveDestroyAPIView):
    permission_classes = [IsReceiverOrSender]
    serializer_class = DirectMessageSerializer
    lookup_url_kwarg = 'direct_message_id'
    lookup_field = 'id'

    def get_queryset(self):
        queryset = DirectMessage.objects.exclude(
            sender=self.request.user.id,
            is_deleted_by_sender=True
        ).exclude(
            receiver=self.request.user.id,
            is_deleted_by_receiver=True
        )
        return queryset

    def perform_destroy(self, instance):
        if self.request.user == instance.receiver:
            instance.is_deleted_by_receiver = True
            instance.save()
        elif self.request.user == instance.sender:
            instance.is_deleted_by_sender = True
            instance.save()

    def get_object(self):
        direct_message = super(DirectMessageDetailView, self).get_object()
        if not direct_message.is_read and self.request.user == direct_message.receiver:
            direct_message.is_read = True
            direct_message.save()

        return direct_message
