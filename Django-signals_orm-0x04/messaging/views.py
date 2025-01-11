from rest_framework import viewsets
from .models import Notification
from .serializers import NotificationSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
class DeleteUserView(APIView):
    permission_classes = [IsAuthenticated]

    def delete_user(self, request):
        user = request.user
        user.delete()
        return Response({"message": "Your account has been deleted successfully."}, status=status.HTTP_200_OK)
