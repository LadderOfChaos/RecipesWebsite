from django import forms
from RecepiesSite.Models.email_sub import Signup


class EmailSignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': "form-control",
        'type': "email",
        'placeholder': 'Your email here',
    }), label='')

    class Meta:
        model = Signup
        fields = ('email',)

