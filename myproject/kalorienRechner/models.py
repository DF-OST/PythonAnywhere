from django.conf import settings
from django.db import models
from datetime import date
from django.utils import timezone

# Create your models here.
class Meal(models.Model):
    name = models.CharField(max_length=50)
    consumed_date = models.DateTimeField(default=timezone.now)
    calorie_count = models.FloatField()

    def consumedToday(self):
        if(self.consumed_date.date() == date.today()):
            return True
        else:
            return False