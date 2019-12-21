from django.contrib import admin

from shrapnel.polls.models import Poll, PollAnswer, PollOption

admin.site.register(Poll)
admin.site.register(PollAnswer)
admin.site.register(PollOption)
