from django.db import models
from django.urls import reverse

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=200)
    when = models.DateTimeField()

    def __str__(self):
        return str(self.name)
    

    def get_absolute_url(self):
        return reverse('events:event-detail', kwargs={'pk': self.pk})