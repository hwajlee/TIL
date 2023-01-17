# board/models.py

from django.db import models

# Create your models here.
class Posting(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    