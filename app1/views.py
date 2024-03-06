from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Reservation
from .forms import ReservationForm, NumberReservation
from django.contrib import messages
from django.views.decorators.http import require_POST

def home(request):
    acompañantes = ['Carlos Camacho','Victor Arellano','Gustavo Gómez', 'Jorge Gómez','David Robles','Ricardo Díaz','Julio Hernandez','Samuel Aguilar','Ulises Ochoa']
    damas = ['Erika Aguilar','Liliana Aguilar','Brenda Gomez','Damaris Gómez', 'Sarahi Aguilar','Alejandra Aguilar','Mahanaim Díaz', 'Daromi Robles', 'Dariana Vazquez', 'Mariana Jimenez']
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        
       
       
        if form.is_valid():
                        
            reservation_code = form.cleaned_data['reservation_code']
            print(form.cleaned_data)
            
          
            try:
                reservation = Reservation.objects.get(reservation_code=reservation_code)
                form = ReservationForm(request.POST, instance=reservation)
                if form.is_valid():
                    form.save()
                    request.session['code_reservation']=reservation_code
                    messages.success(request, 'Tu información ha sido enviada!')
                    url = reverse('app1:successful')
                    return HttpResponseRedirect(url)
                   
            except Reservation.DoesNotExist:
                messages.error(request,'Reservación no encontrada!')
                return render(request, 'not-found.html', {})
                
            
        else:
            messages.error(request, 'No se pudo envíar, trata nuevamente')
    else:
        form = ReservationForm()
    
    return render(request, 'index.html', {'form':form, 'damas':damas, 'acompañantes':acompañantes})

def about(request):
    return render(request, 'about.html', {'name':'Rogelio'})


# def successful_view(request):
#     return render(request, 'form_successful.html', {})

@require_POST
def reservation_not_found(request):
    
    return render(request,'not-found.html',{})


# @require_POST
def successful_form_view(request):
    print(request.session.get('code_reservation'))
    code_reservation = request.session.get('code_reservation')
    reservation = Reservation.objects.get(reservation_code=code_reservation)
    if request.POST:
        form = NumberReservation(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            url = reverse('app1:home')
            return HttpResponseRedirect(url)
    else:
        form = NumberReservation()
    
    
        
    
    
    return render(request, 'form_successful.html',{'form':form, 'reservation':reservation})
    


    