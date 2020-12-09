from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.first_name
