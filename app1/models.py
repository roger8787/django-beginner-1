from django.db import models
import string 
import random

# Create your models here.


class Reservation (models.Model):
    reservation_code = models.CharField(max_length=6, blank=True)
    name = models.CharField(max_length=100)
    num_tickets = models.IntegerField(default=1)
    will_assist = models.BooleanField(default=False)
    message = models.TextField(blank=True, null=True)
    num_will_assist = models.IntegerField(default=1)
    is_reserving_hotel= models.BooleanField(default=False)
    mail = models.EmailField(blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.reservation_code:
            # Generate a random reservation code
            characters = string.digits + string.ascii_letters
            self.reservation_code = ''.join(random.choice(characters) for _ in range(6))
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.reservation_code
    
    
    
    


