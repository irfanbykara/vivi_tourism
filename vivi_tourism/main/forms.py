from django.forms import ModelForm
from .models import Reservation
from django import forms

class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['name','last_name',"address","email","phone","country","city","zip_code"]


