from django.contrib import admin

from shrapnel.topics.models import Topic, Entry, Vote

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Vote)
