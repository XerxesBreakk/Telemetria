from django.db import models
from django.contrib.auth.models import User
import requests

# Create your models here.
class record(models.Model):
    status=models.BooleanField(default=False)
    recordTime=models.DateTimeField(auto_now_add=True)
    setBy=models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    aux=models.BooleanField(default=True)
    
    # def __str__(self):
    #     actStatus="Apagado"
    #     if self.status:
    #         actStatus="Encendido"
    #     return actStatus + " "+ str(self.recordTime)
    
    def lastRecords(n):
        data=record.objects.all().order_by('-id')[:n]
        return data
        
    
    # def sincro():
    #     r=requests.get('http://192.168.10.16/status/')
    #     data=r.json()
    
    