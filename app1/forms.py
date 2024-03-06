from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude='name','num_tickets','num_will_assist','is_reserving_hotel'
        
        widgets={
            'reservation_code':forms.TextInput(attrs={'placeholder':'Enter reservation code', 'class':'form-control bg-secondary border-0 py-4 px-3'}), 
            'message':forms.Textarea(attrs={'class':'form-control bg-secondary border-0 py-2 px-3','placeholder':'Dejale un mensaje a los novios','rows':5}), 
            'will_assist':forms.Select(choices=((True,'Si'), (False,'No')), attrs={'class':'form-control bg-secondary border-0'}),
            'mail':forms.EmailInput(attrs={'class':'form-control bg-secondary border-0 py-4 px-3','placeholder':'Ingresa tu email'})
        }
        


class NumberReservation(forms.ModelForm):
    class Meta:
        model=Reservation
        fields = ['num_will_assist','is_reserving_hotel']
        widgets={
            'num_will_assist':forms.NumberInput(attrs={'class':'form-control bg-secondary border-0 py-4 px-3', 'placeholder':'Ingresa cantidad de asistencias'}),
             'is_reserving_hotel':forms.Select(choices=((True,'Si'), (False,'No')), attrs={'class':'form-control bg-secondary border-0'}),
        }
        
    
   
    