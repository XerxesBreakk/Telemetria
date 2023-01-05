from datetime import timedelta,datetime
from django.db import models
from django.contrib.auth.models import User

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
        data=record.objects.filter(aux=1).order_by('-id')[:n]
        return data
       
    def refreshDelta():
        records=record.objects.filter(aux=1)
        for rec in records:
            nextID=rec.pk +1
            nextRecord=record.objects.get(pk=nextID)
            print(rec.id,' ',rec.status,' ',nextRecord.id,' ',nextRecord.status)
            
            
            if not nextRecord.aux:
                print('Ingreso en if aux')
                nextID=nextID+1
                nextRecord=record.objects.get(pk=nextID)
                
            if rec.status == nextRecord.status:
                nextRecord.aux=0
                nextRecord.descrip='Deshabilitado por repeticion'
                nextRecord.save()
                print('if repeticion de status')
            elif nextRecord.recordTime < rec.recordTime:
                nextRecord.aux=0
                nextRecord.descrip='Deshabilitado por error en recordTime'
                nextRecord.save()
                print('Error en recordTime')
            else:
                delta= nextRecord.recordTime.timestamp() - rec.recordTime.timestamp()
                rec.usedFor=timedelta(seconds=delta)
                # print(str(nextRecord.recordTime))
                # print(str(rec.recordTime))
                # print(rec.usedFor)
                # print(delta)
                rec.save()
                if nextRecord.id==record.objects.latest('id').id:
                    break
    
    # def sincro():
    #     r=requests.get('http://192.168.10.16/status/')
    #     data=r.json()
    
    