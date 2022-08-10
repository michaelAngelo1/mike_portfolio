from django.db import models
from django.utils.timezone import get_current_timezone
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="Description")
    techs = models.CharField(max_length=200, default="HTML")
    date = models.DateField(default=get_current_timezone)

    def __str__(self):
        return self.name

class Achievement(models.Model):
    name = models.CharField(max_length=200, default="Lorem ipsum")
    year = models.CharField(max_length=50, default="2002")
    desc = models.TextField(default="Puspresnas")

    def __str__(self):
        return self.name



