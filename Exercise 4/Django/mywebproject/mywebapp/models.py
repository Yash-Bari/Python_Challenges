from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    skills = models.TextField()

    def __str__(self):
        return self.name
