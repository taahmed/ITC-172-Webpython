from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#ech model will become a table in the databe
class hiphopTracks(models.Model):
    trackname=models.CharField(max_length=255)
    trackdescription=models.CharField(max_length=255)

    def __str__(self):
        return self.trackname

    class Meta:
        db_table='hiphopTracks'

class recordLabels(models.Model):
    recordname=models.CharField(max_length=255)
    hiphopTracks=models.ForeignKey(hiphopTracks,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    madeDate=models.DateField()
    recordURL=models.URLField()
    recorddescription=models.TextField()

    def __str__(self):
        return self.recordname

    class Meta:
            db_table='recordLabels'

    


     