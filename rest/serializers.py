###
### All Serializers follow restful design, see below for notes.
### http://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/#hyperlinking-our-api


from rest_framework import serializers  # Require rest_framework mixin to easily convert classes to JSON.
from django.contrib.auth.models import User, Group  # Permit the login API. Reference: http://www.django-rest-framework.org/tutorial/quickstart/#serializers
from models import (
    RandomBlock, 
    SensorDataBlock,
    PartnerBlock,
    UpdateBlock,
)  # Import all the models we wist to serialize.


### Serializes a Random Block field to JSON.
class RandomBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RandomBlock
        fields = ('Canary', 'DataBlock','DateInitialised','TimeInitialised','pk')


### Serializes the SensorDataBlock to JSON.
class SensorDataBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SensorDataBlock
        fields = ('SensorName', 'SensorDescriptor','SensorValue','DateInitialised','TimeInitialised','pk')


### Serializes the PartnerBlock to JSON.
class PartnerBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PartnerBlock
        fields = ('PartnerName', 'PartnerAddress','PartnerTransmitFreq','PartnerOAUTHTOken','DateInitialised','TimeInitialised','pk')


### Serializes the Update Block to JSON.
class UpdateBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UpdateBlock
        fields = ('UpdateVersion', 'UpdatePath','DateInitialised','TimeInitialised','pk')



### The following classes permit the login auth-api.
### Reference: http://www.django-rest-framework.org/tutorial/quickstart/#serializers
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups','pk')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name','pk')