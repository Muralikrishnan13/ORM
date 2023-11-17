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

 