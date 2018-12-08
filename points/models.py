
from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

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

class Profile(models.Model):
    correo=models.EmailField(primary_key=True)
    name=models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    photo=models.URLField(blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.correo
        
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(name=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
	    instance.userprofile.save()

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
