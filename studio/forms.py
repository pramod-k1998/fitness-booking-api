from django import forms
from .models import Fitness

class BookingForm(forms.Form):
    """
    A form for clients to book a fitness class.
    Requires name, email, and class selection.
    """
    fitness_class = forms.ModelChoiceField(queryset=Fitness.objects.all(),label= "Fitness Class")
    client_name = forms.CharField(max_length=100)
    client_email = forms.EmailField()