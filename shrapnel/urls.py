from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/users/', include(('shrapnel.users.urls', 'users'), namespace='user')),
    re_path(r'^api/polls/', include(('shrapnel.polls.urls', 'polls'), namespace='poll')),
    url(r'^api/', include('shrapnel.topics.urls')),
    url(r'^api/', include('shrapnel.direct_messages.urls')),
]
