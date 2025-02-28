from django.db import models

# Create your models here.
class MenuCategory(models.Model):
    category_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.category_name

class Menu(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    price = models.IntegerField()
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=1, related_name='menus')

    
    def __str__(self):
        return self.name + ' : ' + self.cuisine

