from django.db import models

class Member (models.Model):
    name = models.CharField(max_length=255)
    name_kana = models.CharField(max_length=255)
    nicname = models.CharField(max_length=255)
    official_x_id = models.CharField(max_length=255)
    birthday = models.DateField("birthday",null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    organization = models.ForeignKey('Organization',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

class Organization (models.Model):
    name = models.CharField(max_length=255)
    name_kana = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name