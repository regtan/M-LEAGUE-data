from django.db import models

class Season(models.Model):
    name = models.CharField(max_length=255)
    legular_start_date = models.DateField("legular season start date",null=True,blank=True)
    legular_end_date = models.DateField("legular season end date",null=True,blank=True)
    semifinal_start_date = models.DateField("semifinal start date",null=True,blank=True)
    semifinal_end_date = models.DateField("semifinal end date",null=True,blank=True)
    final_start_date = models.DateField("final start date",null=True,blank=True)
    final_end_date = models.DateField("final end date",null=True,blank=True)