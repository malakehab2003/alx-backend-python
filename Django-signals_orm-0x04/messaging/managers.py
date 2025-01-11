from django.db import models

class unread_for_user(models.Manager):
    def UnreadMessagesManager(self, user):
        return self.filter(receiver=user, read=False)
