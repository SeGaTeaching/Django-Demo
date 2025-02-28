from django.db import models

# Create your models here.
class MangaData(models.Model):
    character = models.CharField(max_length=200)
    manga = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return f'{self.character}, {self.manga}'