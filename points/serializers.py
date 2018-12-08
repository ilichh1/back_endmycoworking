from .models import *
from django.contrib.auth.models import User
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
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ['username', 'email', 'id', 'password']
	def create(self, validated_data):
		password = validated_data.pop('password')
		user = User.objects.create(**validated_data)
		user.set_password(password)
		user.save()

		return user

class ProfileSerializer(serializers.ModelSerializer):
    name=UserSerializer(many=False,read_only=True)
    class Meta:
        model=Profile
        fields='__all__'

class User_teamSerializer(serializers.ModelSerializer):
    profile=ProfileSerializer(many=False, read_only=True)
    profile_id=serializers.PrimaryKeyRelatedField(source='Profile',queryset=Profile.objects.all())
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
    profile=ProfileSerializer(many=False, read_only=True)
    profile_id=serializers.PrimaryKeyRelatedField(source='Profile',queryset=Profile.objects.all())
    coworking=CoworkingSerializer(many=False, read_only=True)
    coworking_id=serializers.PrimaryKeyRelatedField(source='Coworking',queryset=Coworking.objects.all())
    class Meta:
        model=Status
        fields='_all__'
    