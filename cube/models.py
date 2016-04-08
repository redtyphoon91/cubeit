from django.db import models


class User(models.Model):
	name = models.CharField(max_length=100, blank=True, default='',unique=True)
	city = models.CharField(max_length=100, blank=True, default='')
	cubeid = models.IntegerField(default=None,null=True)

class Content(models.Model):
    link = models.CharField(max_length=100, blank=True, default='')

class Cube(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')

class CubeContent(models.Model):
    Cubeid = models.IntegerField()
    Contentid = models.IntegerField()

class UserCont(models.Model):
    Contentid = models.IntegerField()
    Useri = models.IntegerField()

"""
band = cube, musicians = users
if you have a cube model and each cube has several user models related to it,
 then you would put a ForeignKey in the user model.
This way, every user has a cube related to it, and cubes may have users related to them, 
since every user has a cube.
""" 


