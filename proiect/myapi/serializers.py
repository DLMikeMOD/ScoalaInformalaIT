from rest_framework import serializers

from app1.models import Location


class LocationSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Location
        fields = ['city', 'country']
