from django_ical.views import ICalFeed
from prayerweb.models import PrayerTopic

class PrayerFeed(ICalFeed):
    """
    iCal Feed for Prayer Topics
    """
    product_id = '-//'
    timezone = 'UTC'
    
    def items(self):
        return PrayerTopic.objects.all()
    
    def item_title(self, item):
        return item.topic
    
    def item_description(self, item):
        return item.description
    
    def item_start_datetime(self, item):
        return item.date


