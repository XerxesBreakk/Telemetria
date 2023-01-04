from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from .models import record
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets,permissions
from django.contrib.auth.models import User,Group
from .serializers import UserSerializer, GroupSerializer, RecordSerializer
from .forms import LoginForm

# Create your views here.
@login_required(login_url='/API/login/')
def lightStatus(request):
    lastRecord=record.objects.last()
    return render(request,'lightStatus.html',{
        'lastRecord': lastRecord,
        'dataLastRecords': record.lastRecords(10)
    })
    

def lightHistory(request):
    record.refreshDelta()
    return render(request,'lightHistory.html',{
        'records': record.objects.filter(aux=1).order_by('-id')
    })
    
    
class LoginView(FormView):
    form_class = LoginForm
    alert_message = None
    template_name = 'login.html'
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                next = request.GET.get('next')
                if next is not None:
                    return redirect(next)
                return redirect('/')
            else:
                self.alert_message = {'class': 'alert alert-danger',
                'mod': 'Error:',
                'message': u'Cuenta deshabilitada.'}
                return self.get(request)
        else:
            self.alert_message = {'class': 'alert alert-danger',
            'mod': 'Error:',
            'message': u'Usuario o contraseña incorrecta.'}
            return self.get(request)
        return render(request, "/")

    


class LogoutView(LoginView):
    def get(self, request):
        logout(request)
        return super(LogoutView,self).get(request)

    
   
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