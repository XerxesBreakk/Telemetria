from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

import requests

# Create your models here.
class record(models.Model):
    status=models.BooleanField(default=False)
    recordTime=models.DateTimeField(auto_now_add=True)
    setBy=models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    aux=models.BooleanField(default=True)
    descrip=models.CharField(max_length=100,default="No description")
    usedFor=models.DurationField(null=True,blank=True,editable=True)
    
    # def __str__(self):
    #     actStatus="Apagado"
    #     if self.status:
    #         actStatus="Encendido"
    #     return actStatus + " "+ str(self.recordTime)
    
    def lastRecords(n):
        data=record.objects.all().order_by('-id')[:n]
        return data
       
    def refreshDelta():
        records=record.objects.all()
        for rec in records:
            nextID=rec.pk +1
            nextRecord=record.objects.get(pk=nextID)
            delta= nextRecord.recordTime.timestamp() - rec.recordTime.timestamp()
            rec.usedFor=timedelta(seconds=delta)
            print(str(nextRecord.recordTime))
            print(str(rec.recordTime))
            print(rec.usedFor)
            print(delta)
            rec.save()
            try:
                lastRecord=get_object_or_404(records,pk= nextID+1)
            except:
                break
        
    
    # def sincro():
    #     r=requests.get('http://192.168.10.16/status/')
    #     data=r.json()
    
    