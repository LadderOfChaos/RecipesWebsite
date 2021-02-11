from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from users.models import UserProfile

class UserFormMixin():
    def setup_form(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class RegisterForm(UserCreationForm, UserFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=('profile_picture',)




        
        
