from django.shortcuts import render
from .models import record

# Create your views here.
def lightStatus(request):
    lastRecord=record.objects.last()
    print(lastRecord)
    print(record.lastRecords(10))
    return render(request,'lightStatus.html',{
        'lastRecord': lastRecord,
        'dataLastRecords': record.lastRecords(10)
    })
    # return render(request, 'lightStatus.html',{
    #     'lastRecord': lastRecord
    #     'dataLastRecords': record.lastRecords(n)
    # })