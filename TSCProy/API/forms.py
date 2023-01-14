from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(label=u'Contraseña', widget=forms.PasswordInput)
    
    def _init_(self, *args, **kwargs):
        super(LoginForm, self)._init_(*args, **kwargs)
        


class UserCreateForm(UserCreationForm):

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
        
        widgets= {
            'email': forms.EmailInput(
                attrs={
                    'id':"email",
                    'placeholder':"capenafi@espol.edu.ec",
                    'class':"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'id':"username",
                    'placeholder':"Username",
                    'class':"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                }
            ),
            'password1': forms.PasswordInput(
                attrs={
                    'id':"password",
                    'placeholder':"Password",
                    'class':"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                }
            ),
            'password2': forms.PasswordInput(
                attrs={
                    'id':"password2",
                    'placeholder':"Confirm password",
                    'class':"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'id':"first_name",
                    'placeholder':"First name",
                    'class':"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'id':"last_name",
                    'placeholder':"Last name",
                    'class':"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                }
            ),
            'is_superuser': forms.CheckboxInput(
                attrs={
                    'value':'True',
                    'class':"w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600",
                }
            ),
            'is_staff': forms.CheckboxInput(
                attrs={
                    'value':'True',
                    'class':"w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600",
                }
            ),
            
        }
        
class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
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
        widgets= {
            'email': forms.EmailInput(
                attrs={
                    'id':"email",
                    'placeholder':"capenafi@espol.edu.ec",
                    'class':"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'id':"first_name",
                    'placeholder':"First name",
                    'class':"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'id':"last_name",
                    'placeholder':"Last name",
                    'class':"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                }
            ),
            'is_superuser': forms.CheckboxInput(
                attrs={
                    'value':'True',
                    'class':"w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600",
                }
            ),
            'is_staff': forms.CheckboxInput(
                attrs={
                    'value':'True',
                    'class':"w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600",
                }
            ),
            
        }
