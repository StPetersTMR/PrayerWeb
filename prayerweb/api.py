import rest_framework_filters as filters
from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework.views import APIView
from prayerweb.models import PrayerTopic, Week

#Serializers
class PrayerTopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PrayerTopic
        fields = ('topic', 'description', 'date')

class WeekSerializer(serializers.HyperlinkedModelSerializer):
    prayers = PrayerTopicSerializer(many=True, read_only=True)
    class Meta:
        model = Week
        fields = ('sunday', 'image', 'prayers')

#Filter Sets
class PrayerTopicFilter(filters.FilterSet):
    year = filters.DateFilter(name='date__year')
    month = filters.DateFilter(name='date', lookup_type='month')
    date = filters.AllLookupsFilter(name='date')
    class Meta:
        model = PrayerTopic
        fields = ['date', 'year', 'month']

#View Sets
class PrayerTopicViewSet(viewsets.ModelViewSet):
    queryset = PrayerTopic.objects.all()
    serializer_class = PrayerTopicSerializer
    filter_class = PrayerTopicFilter

class WeekViewSet(viewsets.ModelViewSet):
    queryset = Week.objects.all()
    serializer_class = WeekSerializer

