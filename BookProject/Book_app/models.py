from django.db import models
from django.contrib import admin

class Book(models.Model):
    Book_Name = models.CharField(max_length=200)
    Book_ID = models.IntegerField()
    Book_author = models.CharField(max_length=100)
    Book_Issued_date = models.DateField()
    
class BookAdmin(admin.ModelAdmin):
    list_display = ('Book_Name', 'Book_ID', 'Book_author', 'Book_Issued_date')

