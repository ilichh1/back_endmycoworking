from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import viewsets
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class MyUser(APIView):
    def get(self, request, format=None):
        my_user = Profile.objects.all().get(id=request.user.userprofile.id)
        serializer = ProfileSerializer(my_user)
        return Response(serializer.data)
    def put(self, request, format=None):
        my_user = Profile.objects.all().get(id=request.user.userprofile.id)
        serializer = ProfileSerializer(my_user)
        return Response(serializer.data)

class LocationViewSet(viewsets.ModelViewSet):
    queryset=Location.objects.all()
    serializer_class=LocationSerializer

    def get_serializer(self,*args,**kwargs):
        if "data" in kwargs:
            data=kwargs["data"]

            if isinstance(data,list):
                kwargs["many"] =True
        return super(LocationViewSet,self).get_serializer(*args, **kwargs)

class TeamViewSet(viewsets.ModelViewSet):
    queryset=Team.objects.all()
    serializer_class=TeamSerializer

    def get_serializer(self,*args,**kwargs):
        if "data" in kwargs:
            data=kwargs["data"]

            if isinstance(data,list):
                kwargs["many"] =True
        return super(TeamViewSet,self).get_serializer(*args, **kwargs)

class ProfileViewSet(viewsets.ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer

    def get_serializer(self,*args,**kwargs):
        if "data" in kwargs:
            data=kwargs["data"]

            if isinstance(data,list):
                kwargs["many"] =True
        return super(ProfileViewSet,self).get_serializer(*args, **kwargs)


class User_teamViewSet(viewsets.ModelViewSet):
    queryset=User_team.objects.all()
    serializer_class=User_teamSerializer

    def get_serializer(self,*args,**kwargs):
        if "data" in kwargs:
            data=kwargs["data"]

            if isinstance(data,list):
                kwargs["many"] =True
        return super(User_teamViewSet,self).get_serializer(*args, **kwargs)


class LocalViewSet(viewsets.ModelViewSet):
    queryset=Local.objects.all()
    serializer_class=LocalSerializer

    def get_serializer(self,*args,**kwargs):
        if "data" in kwargs:
            data=kwargs["data"]

            if isinstance(data,list):
                kwargs["many"] =True
        return super(LocalViewSet,self).get_serializer(*args, **kwargs)


class SpaceViewSet(viewsets.ModelViewSet):
    queryset=Space.objects.all()
    serializer_class=SpaceSerializer

    def get_serializer(self,*args,**kwargs):
        if "data" in kwargs:
            data=kwargs["data"]

            if isinstance(data,list):
                kwargs["many"] =True
        return super(SpaceViewSet,self).get_serializer(*args, **kwargs)

class CoworkingViewSet(viewsets.ModelViewSet):
    queryset=Coworking.objects.all()
    serializer_class=CoworkingSerializer

    def get_serializer(self,*args,**kwargs):
        if "data" in kwargs:
            data=kwargs["data"]

            if isinstance(data,list):
                kwargs["many"] =True
        return super(CoworkingViewSet,self).get_serializer(*args, **kwargs)

class StatusViewSet(viewsets.ModelViewSet):
    queryset=Status.objects.all()
    serializer_class=StatusSerializer

    def get_serializer(self,*args,**kwargs):
        if "data" in kwargs:
            data=kwargs["data"]

            if isinstance(data,list):
                kwargs["many"] =True
        return super(StatusViewSet,self).get_serializer(*args, **kwargs)
