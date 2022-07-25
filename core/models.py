from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=14)
    msg = models.TextField(max_length=500)

    def __str__(self):
        return self.full_name