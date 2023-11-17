# Ex02 Django ORM Web Application
## Date: 10/10/23

## AIM
To develop a Django application to store and retrieve data from a Football Players database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create 10 Football players

## PROGRAM

```py
Models.py

from django.db import models
from django.contrib import admin
class Player (models.Model):
    pid=models.CharField(max_length=20,help_text="Player ID")
    name=models.CharField(max_length=100)
    salary=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()

class Playeradmin(admin.ModelAdmin):
    list_display=('pid','name','salary','age','email')
    
Admin.py

from django.contrib import admin
from .models import Player,Playeradmin
admin.site.register(Player,Playeradmin)
```
## OUTPUT
![image](https://github.com/Muralikrishnan13/ORM/assets/130058615/44d01b26-2947-4138-b2a8-4a1c6f5973f2)
![image](https://github.com/Muralikrishnan13/ORM/assets/130058615/df179c3d-65ae-4792-b734-3157be11d92d)




## RESULT
Thus the program for creating a database using ORM hass been executed successfully
