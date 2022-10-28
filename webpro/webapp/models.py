from django.db import models

# Create your models here.
class Arithmetic(models.Model):
    sum = models.IntegerField()
    sub = models.IntegerField()
    mul = models.IntegerField()
    div = models.IntegerField()

    def __str__(self):
        return self.sum