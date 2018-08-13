from django.db import models


# Create your models here.

class Course(models.Model):
    code = models.CharField(max_length=5, null=False, primary_key=True)
    title = models.CharField(max_length=30, null=False, unique=True)
    duration = models.IntegerField(null=False)
    fee = models.IntegerField(null=False)

    def __str__(self):
        return self.title