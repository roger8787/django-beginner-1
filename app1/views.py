from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {'name':'rogelio'})

def about(request):
    return render(request, 'about.html', {'name':'Rogelio'})