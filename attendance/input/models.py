from django.db import models
import datetime
# Create your models here.
class Attendance(models.Model):
    subj=[]
    for sub in ['MPA','HRM','IT','ECO','ECOMM','HRM' 'TUT','ECO TUT','IT TUT','MPA TUT']:
        subj.append((sub,sub))
    subs=models.CharField(max_length=10,choices=subj)
    status=models.BooleanField()
    date = models.DateField( default=datetime.date.today)
