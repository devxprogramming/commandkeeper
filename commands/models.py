from django.db import models
from django.contrib.auth.models import User
import uuid


levels = (
    ('INFO', 'INFO'),
    ('WARNING', 'WARNING'),
    ('ERROR', 'ERROR'),
    ('CRITICAL', 'CRITICAL'),
)

class Command(models.Model):
    cid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    command = models.TextField()
    tag = models.CharField(max_length=100)
    level = models.CharField(max_length=100, choices=levels)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)