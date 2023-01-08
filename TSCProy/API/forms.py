from django import forms
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(label=u'Contraseña', widget=forms.PasswordInput)
    
    def _init_(self, *args, **kwargs):
        super(LoginForm, self)._init_(*args, **kwargs)
        


class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'is_active',
            'is_staff',
            'is_superuser',
             'groups',
        )
        exclude =('password',
           
            'user_permissions' )
        
class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'is_superuser',
             'groups',
        )
        exclude=(
            'password',
        )
