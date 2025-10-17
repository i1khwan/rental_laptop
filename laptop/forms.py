from django import forms
from .models import Booking
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox


class BookingForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    class Meta:
        model = Booking
        fields = ['customer_name', 'customer_address', 'rental_date', 'location_pin', 'captcha']
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nama lengkap',
                'required': 'required'
            }),
            'customer_address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan alamat lengkap',
                'required': 'required'
            }),
            'rental_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'required': 'required'
            }),
            'location_pin': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan kode lokasi',
                'required': 'required'
            }),
        }
