from django.db import models

# Create your models here.
class Strawhats(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    member = models.CharField(max_length=300)
    gender = models.CharField(
        choices=[('M', 'male'), ('F', 'female')],
        default='M',
        max_length=1
    )
    
    def __str__(self) -> str:
        return f'{self.name}, {self.position}'