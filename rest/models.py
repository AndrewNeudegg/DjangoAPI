# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

### NB: DATE/TIME Auto initalising idea influenced by: http://stackoverflow.com/questions/11385607/how-to-model-a-timefield-in-django @ S/O User:César


### Contains Random Data.
class RandomBlock(models.Model):
    Canary = models.CharField(max_length=6)  # Should this service ever need to stop sending the Canary flag. It can. Via Rest.
    DataBlock = models.CharField(max_length=4096)  # This shouldn't be this large, the padding is for string increase due to encryption.
    DateInitialised = models.DateField(auto_now_add=True, blank=True)  # Date Initialised.
    TimeInitialised = models.TimeField(auto_now_add=True, blank=True)  # Time Initialised. 

### Holds sensor informtaion, including values.
class SensorDataBlock(models.Model):
    SensorName = models.CharField(max_length=10)
    SensorDescriptor = models.CharField(max_length=20)    
    SensorValue = models.DecimalField(max_digits=20, decimal_places=10)
    DateInitialised = models.DateField(auto_now_add=True, blank=True)  # Date Initialised.
    TimeInitialised = models.TimeField(auto_now_add=True, blank=True)  # Time Initialised. 

### Describes this devices relationship to other devices.
class PartnerBlock(models.Model):
    PartnerName = models.CharField(max_length=20)
    PartnerAddress = models.CharField(max_length=100)  # Field could be an IP, rest API or URI/URL.
    PartnerTransmitFreq = models.IntegerField()  # Length of time in MS between each transmit / check. Non Compulsory.
    PartnerOAUTHTOken = models.CharField(max_length=50)  # Store the OAUTH token granted to this client.
    DateInitialised = models.DateField(auto_now_add=True, blank=True)  # Date Initialised.
    TimeInitialised = models.TimeField(auto_now_add=True, blank=True)  # Time Initialised. 

### Permits non local updates.
class UpdateBlock(models.Model):
    UpdateVersion = models.CharField(max_length=20)  # Semantically Named update versioning.
    UpdatePath = models.CharField(max_length=100)  # Path to the upgrade, URI/URL.
    DateInitialised = models.DateField(auto_now_add=True, blank=True)  # Date Initialised.
    TimeInitialised = models.TimeField(auto_now_add=True, blank=True)  # Time Initialised. 

