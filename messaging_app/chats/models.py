from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
  user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  first_name = models.CharField(null=False)
  last_name = models.CharField(null=False)
  email = models.EmailField(unique=True, null=False, db_index=True)
  password_hash = models.CharField(null=False)
  phone_number = models.CharField(null=True)
  role = models.CharField(choices=[('guest', 'Guest'), ('host', 'Host'), ('admin', 'Admin')], null=False)
  created_at = models.DateTimeField(auto_now=True)


class Conversation(models.Model):
  conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
  participants = models.ManyToManyField(User, related_name='conversations')
  created_at = models.DateTimeField(auto_now=True)


class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    message_body = models.TextField(null=False)
    sent_at = models.DateTimeField(auto_now_add=True)