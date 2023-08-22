from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50, unique=True)
    camelValue = models.IntegerField()

    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    body = models.CharField(max_length=50)
    iq = models.IntegerField()
    hair = models.CharField(max_length=50)
    beard = models.CharField(max_length=50)
    jewlery = models.CharField(max_length=50)

    def getCamelValue(self):
        return self.camelValue
