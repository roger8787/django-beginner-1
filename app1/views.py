from django.shortcuts import get_object_or_404, redirect, render
from .models import Reservation
from .forms import ReservationForm
from django.contrib import messages
from django.views.decorators.http import require_POST

def home(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST,)
       
       
        if form.is_valid():
            
            reservation_code = form.cleaned_data['reservation_code']
            
          
            try:
                reservation = Reservation.objects.get(reservation_code=reservation_code)
                form = ReservationForm(request.POST, instance=reservation)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Tu información ha sido enviada!')
                    return render(request, 'form_successful.html', {'reservation':reservation})
            except Reservation.DoesNotExist:
                messages.error(request,'Reservación no encontrada!')
                return render(request, 'not-found.html', {})
                
            
        else:
            messages.error(request, 'No se pudo envíar, trata nuevamente')
    else:
        form = ReservationForm()
    
    return render(request, 'index.html', {'form':form})

def about(request):
    return render(request, 'about.html', {'name':'Rogelio'})


# def successful_view(request):
#     return render(request, 'form_successful.html', {})

@require_POST
def reservation_not_found(request):
    return render(request,'not-found.html',{})


@require_POST
def successful_form_view(request):
    return render(request, 'form-successful.html',{})
    


    