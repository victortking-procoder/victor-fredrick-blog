from django.urls import path
from .views import MessageCreateView, MessageListView, MessageDetailView

urlpatterns = [
    path('messages/', MessageListView.as_view(), name='message-list'),       # admin only
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),  # admin only
    path('contact/', MessageCreateView.as_view(), name='contact'),            # public form submission
]