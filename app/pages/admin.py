from django.contrib import admin
from .models import Food


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'food_type', 'image')
    list_display_links = ('name', 'price', 'description', 'food_type')


admin.site.register(Food, FoodAdmin)
