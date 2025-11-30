from django.db import models
from django.conf import settings


class Idea(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, default='pending', max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ideas')
    collaborators = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='collaborations')
    tags = models.CharField(blank=True, max_length=200)

    def __str__(self):
        return self.title


class CollaborationRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name='collab_requests')
    requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_collab_requests')
    message = models.TextField(blank=True)
    status = models.CharField(choices=STATUS_CHOICES, default='pending', max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.requester} -> {self.idea} ({self.status})"
