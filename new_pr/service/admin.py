from dataclasses import field
from modulefinder import Module
from django.contrib import admin

# Register your models here.

from .models import Product, Bin

#admin.site.register(Product)
admin.site.register(Bin) 

@admin.register(Product) #декоратор
class ProductAdmin(admin.ModelAdmin):
    list_display= ['id','title','coast']
    fields = ['title', 'coast'] #выводимые поля внутри карточки
    list_filter = ['coast'] #фильрация по полю
    search_fields = ['title'] #поиск по полю
 
#admin.site.register(Product, ProductAdmin)