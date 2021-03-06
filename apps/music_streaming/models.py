# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login.models import User

class Interest(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=1) # 'i' for instrument, 'g' for genre
    users = models.ManyToManyField(User, related_name='interests')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class InterestInstrument(models.Model):
    interest = models.OneToOneField(Interest, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class InterestGenre(models.Model):
    interest = models.OneToOneField(Interest, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Artist(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(blank=True)
    followers = models.ManyToManyField(User, related_name='follows_artist')
    artist_image = models.ImageField(upload_to='artistimages/', default='defaultartist.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Album(models.Model):
    name = models.CharField(max_length=255)
    releaseyear = models.IntegerField()
    artists = models.ManyToManyField(Artist, related_name='artists')
    interests = models.ManyToManyField(InterestGenre, related_name='albums')
    album_image = models.ImageField(upload_to='albumimages/', default='defaultalbum.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='track_album', default=0)
    title = models.CharField(max_length=255)
    tracknumber = models.IntegerField()
    length = models.IntegerField(null=True, blank=True) # length in seconds
    location = models.FileField(upload_to='music/')
    interests = models.ManyToManyField(Interest, related_name='tracks', blank=True)
    followers = models.ManyToManyField(User, related_name='follows_track', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    playlistjson = models.TextField(blank=True) # stored as JSON data - note https://docs.python.org/2/library/json.html#encoders-and-decoders
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
