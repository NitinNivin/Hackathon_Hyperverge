from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Flashcard, Badge

@receiver(post_save, sender=Flashcard)
def create_badge(sender, instance, created, **kwargs):
    if created:
        # Assuming you have a way to get the user who answered the flashcard
        user = User.objects.get(username='example_user')
        Badge.objects.create(user=user, flashcard=instance)
