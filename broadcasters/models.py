from django.db import models
from organizations.models import Organization

class Broadcaster(models.Model):    
    name = models.CharField(max_length=255)
    organization = models.ForeignKey('organizations.Organization', on_delete=models.CASCADE,null=True)
    official_x_id = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True, blank=True)