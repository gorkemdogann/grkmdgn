from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "phone","message"]
        widgets = {
            'name' : forms.TextInput(
                attrs={
                    'placeholder':'İsim'
                }
            ),
            'email' : forms.EmailInput(
                attrs={
                    'placeholder':'E-mail Adresiniz'
                }
            ),
            'phone' : forms.TextInput(
                attrs={
                    'placeholder':'Telefon Numaranız'
                }
            ),
            'message' : forms.TextInput(
                attrs={
                    'placeholder':'Mesajınız'
                }
            ),
        }