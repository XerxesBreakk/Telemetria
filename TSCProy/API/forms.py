from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(label=u'Contraseña', widget=forms.PasswordInput)
    
    def _init_(self, *args, **kwargs):
        super(LoginForm, self)._init_(*args, **kwargs)