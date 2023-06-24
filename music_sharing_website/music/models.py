from django.db import models
from django.contrib.auth.models import User

class MusicFile(models.Model):
    VISIBILITY_CHOICES = (
        ('public', 'Public'),
        ('private', 'Private'),
        ('protected', 'Protected'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='music_files/')
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES)
    allowed_emails = models.TextField(blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username