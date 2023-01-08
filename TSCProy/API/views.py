from django.http import Http404
from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import Group, Permission
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeletionMixin
from django.urls import reverse_lazy
from .models import record
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets,permissions
from .serializers import UserSerializer, GroupSerializer, RecordSerializer
from .forms import LoginForm

from django.contrib.auth.models import User,Group
from .forms import LoginForm,UserCreationForm,UserChangeForm
from django.contrib.auth.views import update_session_auth_hash

# Create your views here.
@login_required(login_url='/API/login/')
def lightStatus(request):
    lastRecord=record.objects.last()
    return render(request,'lightStatus.html',{
        'lastRecord': lastRecord,
        'dataLastRecords': record.lastRecords(10)
    })
    

def lightHistory(request):
    #record.refreshDelta()
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
            print(self.alert_message['message'])
            return self.get(request)
        return render(request, "/")
    
    def get_context_data(self, **kwargs):
        context=super(LoginView,self).get_context_data( **kwargs)
        context['message']=self.alert_message
        return context
            
        
        

    


class LogoutView(LoginView):
    def get(self, request):
        logout(request)
        return super(LogoutView,self).get(request)

    
   
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]
    

class RecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class PermissionsListView(UserPassesTestMixin, ListView):
    model = Permission
    template_name = 'permissions_list.html'

    
    def test_func(self):
        return self.request.user.is_superuser
    

class UserListView(UserPassesTestMixin, ListView):
    model = User
    template_name = 'user_list.html'

    
    def test_func(self):
        return self.request.user.is_superuser
    
class UserCreate(UserPassesTestMixin, CreateView):
    form_class=UserCreationForm
    template_name = 'user_create.html'
    success_url = '/API/user/'

    
    def test_func(self):
        return self.request.user.is_superuser
    
    def form_valid(self, form):
        try:
            context = self.get_context_data()
            userprofile = context['userprofile']

            if not User.objects.filter(username=form.instance.username).exists() and userprofile.is_valid():
                self.object = form.save()
                for group_ in form.cleaned_data['groups']:
                    self.object.groups.add(group_)
                response = super(UserCreate, self).form_valid(form)
            else:
                response = super(UserCreate, self).form_invalid(form)
        except Exception as e:
            response = super(UserCreate, self).form_invalid(form)
        return response

    
    def form_invalid(self, form):
        return super(UserCreate, self).form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super(UserCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['userprofile'] = UserCreationForm(self.request.POST)
        else:
            context['userprofile'] = UserCreationForm()
        return context
    
class UserUpdate(UserPassesTestMixin, UpdateView):
    form_class=UserChangeForm
    template_name = 'user_create.html'
    success_url = '/API/user/'

    
    def test_func(self):
        return self.request.user.is_superuser

    
    def get_object(self, queryset=None):
        if not User.objects.filter(pk=self.kwargs['id']).exists():
            raise Http404
        user = User.objects.get(pk=self.kwargs['id'])
        return user
    
    def form_valid(self, form):
        try:
            print("Form valid")
            if form.is_valid():
                print("Es valido")
                self.object = form.save()
                for group_ in form.cleaned_data['groups']:
                    self.object.groups.add(group_)
                response = super(UserUpdate, self).form_valid(form)
            else:
                response = super(UserUpdate, self).form_invalid(form)
        except Exception as e:
            response = super(UserUpdate, self).form_invalid(form)
        return response

    
    def form_invalid(self, form):
        print("Form Invalid")
        return super(UserUpdate, self).form_invalid(form)
    
    
    def get_context_data(self, **kwargs):
        context = super(UserUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['userprofile'] = UserChangeForm(self.request.POST)
        else:
            context['userprofile'] = UserChangeForm()
        return context
    
class UserDeleteView(UserPassesTestMixin,UpdateView):
    model=User
    template_name='delete_user.html'
    success_url=reverse_lazy('UserListView')
    fields='__all__'
    
    def test_func(self):
        return self.request.user.is_superuser
    
    def get_object(self, queryset=None):
        if not User.objects.filter(pk=self.kwargs['id']).exists():
            raise Http404
        user = User.objects.get(pk=self.kwargs['id'])
        return user
    
    def form_valid(self, form):
        try:
            print(form.instance.id)
            print(form.cleaned_data['id'])
            print(form.cleaned_data['username'])
            user = User.objects.get(pk=form.instance.id)
            user.is_active = False
            user.save()
            response = super(UserUpdate, self).form_valid(form)
        except Exception as e:
            response = super(UserUpdate, self).form_invalid(form)
        return response
    
    def post(self,request,id):
        try:
            user=User.objects.get(pk=id)
            user.is_active=False
            user.save()
            print("Usuario eliminado")
            return redirect('UserListView')
            
        except Exception as e:
            return redirect('/')
    
    
    
    
class GroupListView(UserPassesTestMixin, ListView):
    model = Group
    template_name = 'group_list.html'

    
    def test_func(self):
        return self.request.user.is_superuser
    
class GroupCreate(UserPassesTestMixin, CreateView):
    model = Group
    fields = '__all__'
    template_name = 'group_create.html'
    success_url = '/API/group/'

    
    def test_func(self):
        return self.request.user.is_superuser
    
class GroupUpdate(UserPassesTestMixin, UpdateView):
    model = Group
    fields = '__all__'
    template_name = 'group_create.html'
    success_url = '/API/group/'

    
    def test_func(self):
        return self.request.user.is_superuser

    
    def get_object(self, queryset=None):
        if not Group.objects.filter(pk=self.kwargs['id']).exists():
            raise Http404
        group = Group.objects.get(pk=self.kwargs['id'])
        print(group)
        return group

    
    def get_context_data(self, **kwargs):
        context = super(GroupUpdate, self).get_context_data(**kwargs)
        context['tittle'] = "Grupos de Roles"
        context['motto'] = "Formulario para editar un Grupo de Roles existente"

        form = context['form']
        for field in form.fields:
            form.fields[field].widget.attrs['class'] = 'form-control'
            if form.fields[field].help_text:
                form.fields[field].widget.attrs['data-toggle'] = 'tooltip'
                form.fields[field].widget.attrs['data-placement'] = 'top'
                form.fields[field].widget.attrs['title'] = form.fields[field].help_text
        return context