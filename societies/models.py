from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class Society(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Member(models.Model):
    member_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    contact = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    society = models.ManyToManyField(Society, blank=True)

    def __str__(self):
        return self.name

    def clean(self, *args, **kwargs):
        if self.society.count() > 3:
            raise ValidationError("You can't assign to more than three societies")
        super(Member, self).clean(*args, **kwargs)
