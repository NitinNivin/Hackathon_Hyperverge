from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Flashcard(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question



    def is_expired(self):
        # Check if the badge is expired (created more than 3 days ago)
        return timezone.now() - self.created_at > timezone.timedelta(days=3)

