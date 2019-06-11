from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#the model will become a table in the databe
class MediaType(models.Model):
    typename= models.CharField(max_length=255) 
    mediatypedescription= models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.typename
    class Meta:
        db_table='mediatype'
class Tracks(models.Model):
    trackno=models.CharField(max_length=255)
    tracktitle=models.CharField(max_length=255)
    trackdistributor=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    tracktype=models.ForeignKey(MediaType,on_delete=models.CASCADE)
    def __str__(self):
        return self.tracktitle
    class Meta:
        db_table='tracks'

class RecordLabels(models.Model):
    recordname=models.CharField(max_length=255)
    tracks=models.ForeignKey(Tracks,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    recorddate=models.DateField()
    recordURL=models.URLField()
    recorddescription=models.TextField()

    def __str__(self):
        return self.recordname
    class Meta:
            db_table='recordLabels'