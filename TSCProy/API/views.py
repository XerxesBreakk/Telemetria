from django.shortcuts import render
from .models import record
from rest_framework import viewsets,permissions
from django.contrib.auth.models import User,Group
from .serializers import UserSerializer, GroupSerializer, RecordSerializer

# Create your views here.
def lightStatus(request):
    lastRecord=record.objects.last()
    return render(request,'lightStatus.html',{
        'lastRecord': lastRecord,
        'dataLastRecords': record.lastRecords(10)
    })
    

def lightHistory(request):
    record.refreshDelta()
    return render(request,'lightHistory.html',{
        'records': record.objects.all().order_by('-id')
    })
   
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class RecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [permissions.IsAuthenticated]