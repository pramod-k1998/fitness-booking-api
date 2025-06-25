from django import forms
from .models import Fitness

class BookingForm(forms.Form):
    fitness_class = forms.ModelChoiceField(queryset=Fitness.objects.all(),label= "Fitness Class")
    client_name = forms.CharField(max_length=100)
    client_email = forms.EmailField()