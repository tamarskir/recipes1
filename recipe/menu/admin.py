from django.contrib import admin
from .models import  Recipe, Category, Messages




class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name')

class MesssgesAdmin(admin.ModelAdmin):
    list_display = ('date', 'message')



admin.site.register(Recipe)
admin.site.register(Messages)

admin.site.register(Category)