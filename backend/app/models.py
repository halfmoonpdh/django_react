from django.db import models
from django.utils.timezone import now

# Create your models here.


class DemoUser(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=30)
    age = models.IntegerField()
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    married = models.BooleanField()
    group = models.CharField(max_length=30)
    joined = models.DateTimeField(default=now, editable=False)


class Poster(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=100)
    detail = models.TextField()
    writer = models.ForeignKey(DemoUser, on_delete=models.CASCADE)
    created = models.DateTimeField(default=now, editable=True)
