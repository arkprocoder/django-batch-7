from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone_number=models.CharField(max_length=12)
    description=models.TextField(max_length=250)

    def __str__(self):
        return self.name
    