from django.urls import path
from . import views

app_name = 'app1'
urlpatterns = [
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'), 
    # path('successful/', views.successful_view, name='successful'),
    path('not-found/', views.reservation_not_found, name='not-found'),  
]
