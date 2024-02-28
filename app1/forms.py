from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude='name','num_tickets'
        
        widgets={
            'reservation_code':forms.TextInput(attrs={'placeholder':'Enter reservation code', 'class':'form-control'}), 
            'message':forms.Textarea(attrs={'class':'form-control',}), 
            'will_assist':forms.Select(choices=((True,'Yes'), (False,'No')), attrs={'class':'form-control'})
        }