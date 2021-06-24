from django.db import models

# Create your models here.

class myreviews(models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField()