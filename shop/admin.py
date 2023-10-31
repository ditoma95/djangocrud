from django.contrib import admin

from shop.models import Category, Product

# Register your models here.

#Fixons les attributs qui seront visible par l'utilisateur
class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'date_added')

class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'description', 'category', 'date_added')








admin.site.register(Category, AdminCategory)
admin.site.register(Product, AdminProduct)
