from django.contrib import admin

from prayerweb.models import PrayerTopic, Week
# Register your models here.

@admin.register(PrayerTopic)
class PrayerTopicAdmin(admin.ModelAdmin):
    fields = ('topic', 'description', 'date')
    list_display = ('date', 'topic')
    search_fields = ('topic', )
    list_filter = ('date', )

@admin.register(Week)
class WeekAdmin(admin.ModelAdmin):
    fields = ('sunday', 'image')
    list_display = ('__str__', )
    list_filter = ('sunday', )
