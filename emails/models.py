from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

# Create your models here.
class BulkEmail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200, blank=True)
    content = models.TextField(max_length=5000, blank=True)
    recipients = ArrayField(
        models.EmailField(),
        blank = True,
    )
    activated = models.BooleanField(default=False)

    def __str__(self):
        return self.title