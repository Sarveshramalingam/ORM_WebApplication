# Ex01 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 5 Car 

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import Vehicle
class CarAdmin(admin.ModelAdmin):
    list_display = ['car_name', 'car_type', 'car_price', 'car_year']
    search_fields = ['car_name', 'car_type']
admin.site.register(Vehicle, CarAdmin)

models.py

from django.db import models

class Vehicle(models.Model):
    car_name = models.CharField(max_length=100)
    car_type = models.CharField(max_length=100)
    car_price = models.IntegerField()
    car_year = models.PositiveIntegerField()

    def str(self):
        return (f"{self.car_name} {self.car_type} {self.car_price} {self.car_year}")
```
## OUTPUT

<img width="1896" height="909" alt="Screenshot 2025-09-24 214310" src="https://github.com/user-attachments/assets/6fec1df8-cbec-4311-8d6a-1ac29df17a71" />


## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
