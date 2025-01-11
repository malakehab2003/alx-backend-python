from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Message, Notification, MessageHistory

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.receiver,
            message=instance,
        )

@receiver(pre_save, sender=Message)
def save_before_edit(sender, instance, created, **kwargs):
    if instance.pk:
        old_message = Message.objects.get(pk=instance.pk)
        MessageHistory.objects.create(
            message = instance,
            old_content = old_message.content,
        )
        instance.edited = True