from django.conf.urls import patterns, include, url
from rest_framework import routers
from prayerweb.api import PrayerTopicViewSet, WeekViewSet

#API Router

router = routers.DefaultRouter()
router.register(r'topics', PrayerTopicViewSet)
router.register(r'weeks', WeekViewSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
