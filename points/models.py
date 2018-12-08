
from __future__ import unicode_literals
from django.db import models

class Location(models.Model):
    adress=models.TextField()
    latitude=models.IntegerField(blank=True,null=True)
    longitud=models.IntegerField(blank=True,null=True)
    def __str__(self):
        return "{}".format(self.adress)

class Team(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name

class User(models.Model):
    correo=models.EmailField(primary_key=True)
    name=models.CharField(max_length=50)
    photo=models.URLField(blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name

class User_team(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    team=models.ForeignKey(Team,on_delete=models.CASCADE)
    def __str__(self):
        return '{} in team:{}'.format(self.user,self.team)

class Local(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(blank=True,null=True)
    banner=models.URLField(blank=True,null=True)
    location=models.ForeignKey(Location,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Space(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(blank=True,null=True)
    banner=models.URLField(blank=True,null=True)
    local=models.ForeignKey(Local,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Coworking(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(blank=True,null=True)
    banner=models.URLField(blank=True,null=True)
    init_hour=models.DateTimeField()
    final_hour=models.DateTimeField()
    space=models.ForeignKey(Space,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
        
class Status(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    coworking=models.ForeignKey(Coworking, on_delete=models.CASCADE)
    status=models.CharField(max_length=50)
    def __str__(self):
        return self.name
