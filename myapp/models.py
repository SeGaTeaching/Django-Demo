from django.db import models

# Create your models here.
class Person(models.Model):
    Person_Name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    url = models.URLField()
    
    def __str__(self):
        return f'{self.Person_Name}, {self.email}, {self.url}'

class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=100)
    arrival_time = models.DateTimeField()
    guest_count = models.IntegerField()
    notes = models.TextField()
    class Meta:
        permissions = [('can_change_category', 'Can change category')]
    
    def __str__(self) -> str:
        return self.customer_name