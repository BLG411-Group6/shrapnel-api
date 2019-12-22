from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated

from .models import Poll, PollOption
from .serializers import PollSerializer, PollAnswerSerializer, PollOptionSerializer


class PollsView(ListCreateAPIView):
    queryset = Poll.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PollSerializer


class PollDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PollSerializer
    lookup_url_kwarg = 'pk'


class PollOptionsView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PollOptionSerializer

    def get_queryset(self):
        return PollOption.objects.filter(poll_id=self.kwargs['poll_id'])

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['poll'] = Poll.objects.get(id=self.kwargs['poll_id'])
        return context


class PollAnswerView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PollAnswerSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        poll = get_object_or_404(Poll, id=self.kwargs['poll_id'])
        poll_option = get_object_or_404(PollOption, poll=poll, id=self.kwargs['option_id'])
        context['poll'] = poll
        context['option'] = poll_option
        return context
