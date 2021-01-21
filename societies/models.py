from django.db import models

# Create your models here.
class Society(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    members = models.ManyToManyField('Member')

    def __str__(self):
        return self.name
class Member(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    contact = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.name

