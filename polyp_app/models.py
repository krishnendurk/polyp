from django.db import models


class DatasetTable(models.Model):
    id = models.AutoField(primary_key=True)
    class_name= models.CharField(max_length=100)    
    image = models.FileField()
    is_trained = models.BooleanField(default=False)


class DetectionTable(models.Model):
    id = models.AutoField(primary_key=True)      
    image = models.FileField()
    detected = models.CharField(max_length=10,blank = True, null=True)
 
