from django.db import models

class unread_for_user(models.Manager):
    def get_unread_messages(self, user):
        return self.filter(receiver=user, read=False).only('id', 'sender', 'content', 'timestamp')
