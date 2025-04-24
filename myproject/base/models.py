from django.db import models

# Create your models here.


class HealthForm(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
    
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    state = models.CharField(max_length=100)
    aadhaar_number = models.CharField(max_length=12, unique=True)
    email = models.EmailField(unique=True)
    health_problem = models.TextField()
    date_of_visit = models.DateField(auto_now_add=True)
