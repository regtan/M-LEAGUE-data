from django.db import models

class Organization (models.Model):
    name = models.CharField(max_length=255)
    name_kana = models.CharField(max_length=255)
    official_x_id = models.CharField(max_length=255,null=True,blank=True)
    site_url = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name