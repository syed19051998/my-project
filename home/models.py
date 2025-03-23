from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=13)
    desc = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.phone} - {self.date}"
