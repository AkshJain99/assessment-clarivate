from django.db import models

class Users(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=100)

class Settings(models.Model):
    IsNotificationEnabled = models.BooleanField(default=True)
    IsNewDashboardEnabled = models.BooleanField(default=False)
    Timezone = models.CharField(max_length=50)
