from django.db import models
from datetime import date, timedelta
from prayerweb.validators import validate_sunday

# Create your models here.

class PrayerTopic(models.Model):
    topic = models.CharField(max_length=128)
    description = models.TextField()
    date = models.DateField(unique=True)
    def __str__(self):
        return "{0}: {1}".format(self.date, self.topic)

class Week(models.Model):
    sunday = models.DateField(validators=[validate_sunday])
    image = models.ImageField()
    def __str__(self):
        isocal = self.sunday.isocalendar()
        return "{0}: Week {1}".format(isocal[0], isocal[1])
    def prayers(self):
        return PrayerTopic.objects.filter(date__gte=self.sunday, date__lte=self.end_date())
    def end_date(self):
        return self.sunday + timedelta(days=6)
