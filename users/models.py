from django.db import models

# Create your models here.
class Profile(models.Model):
    email = models.EmailField()
    fullname = models.CharField(max_length=70)
    dob = models.DateField()