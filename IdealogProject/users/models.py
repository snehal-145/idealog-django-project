from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import OperationalError, ProgrammingError

class Profile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return f"{self.user.username} ({self.role})"

# Automatically create/update Profile when User is created
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    # The profile table may not exist yet during early development (migrations not applied).
    # Wrap in try/except to avoid raising OperationalError to the view; migrations should be applied
    # as the correct fix so the Profile table exists.
    try:
        if created:
            Profile.objects.create(user=instance)
        # attempt to save the related profile (will fail if table missing)
        instance.profile.save()
    except (OperationalError, ProgrammingError):
        # Database table for Profile does not exist yet — skip for now.
        # The developer should run `manage.py migrate` to create the table.
        return
