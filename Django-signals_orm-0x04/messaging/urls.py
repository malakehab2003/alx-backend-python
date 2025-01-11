from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotificationViewSet, DeleteUserView, ThreadedConversationView

router = DefaultRouter()
router.register(r'notifications', NotificationViewSet, basename='notification')

urlpatterns = [
    path('', include(router.urls)),
    path('delete-account/', DeleteUserView.as_view(), name='delete_account'),
    path('conversations/<int:conversation_id>/', ThreadedConversationView.as_view(), name='threaded_conversation'),
]
