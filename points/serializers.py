from .models import *
from rest_framework import serializers

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model= Location
        fields='__all__'

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model= Team
        fields= '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields='__all__'

class User_teamSerializer(serializers.ModelSerializer):
    user=UserSerializer(many=False, read_only=True)
    user_id=serializers.PrimaryKeyRelatedField(source='User',queryset=User.objects.all())
    team=TeamSerializer(many=False,read_only=True)
    team_id=serializers.PrimaryKeyRelatedField(source='Team',queryset=Team.objects.all())
    
    class Meta:
        model=User_team
        fields='__all__'

class LocalSerializer(serializers.ModelSerializer):
    location=LocationSerializer(many=False, read_only=True)
    location_id=serializers.PrimaryKeyRelatedField(source='Location',queryset=Location.objects.all())

    class Meta:
        model=Local
        fields='__all__'

class SpaceSerializer(serializers.ModelSerializer):
    local=LocalSerializer(many=False, read_only=True)
    local_id=serializers.PrimaryKeyRelatedField(source='Local',queryset=Local.objects.all())

    class Meta:
        model=Space
        fields='__all__'

class CoworkingSerializer(serializers.ModelSerializer):
    space=SpaceSerializer(many=False,read_only=True)
    space_id=serializers.PrimaryKeyRelatedField(source='Space',queryset=Space.objects.all())

    class Meta:
        model=Coworking
        fields='__all__'

class StatusSerializer(serializers.ModelSerializer):
    user=UserSerializer(many=False, read_only=True)
    user_id=serializers.PrimaryKeyRelatedField(source='User',queryset=User.objects.all())
    coworking=CoworkingSerializer(many=False, read_only=True)
    coworking_id=serializers.PrimaryKeyRelatedField(source='Coworking',queryset=Coworking.objects.all())
    class Meta:
        model=Status
        fields='_all__'
    