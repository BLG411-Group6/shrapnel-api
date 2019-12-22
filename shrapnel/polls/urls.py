from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.PollsView.as_view(), name='polls'),
    path(r'<int:pk>/', views.PollDetailView.as_view(), name='poll-detail'),
    path(r'<int:poll_id>/options/', views.PollOptionsView.as_view(), name='poll-options'),
    path(r'<int:poll_id>/options/<int:option_id>/answer/', views.PollAnswerView.as_view(), name='poll-answers'),
]
