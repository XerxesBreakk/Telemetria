from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import record


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = record
        fields=['id','status','recordTime','setBy','aux','descrip']