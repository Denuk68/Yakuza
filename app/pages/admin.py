from django.contrib import admin
from .models import Pizza, Sushi, Dessert, New


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image')
    list_display_links = ('name', 'price', 'description')


class SushiAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image')
    list_display_links = ('name', 'price', 'description')


class DessertAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image')
    list_display_links = ('name', 'price', 'description')
    

class NewAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image')
    list_display_links = ('name', 'price', 'description')


admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Sushi, SushiAdmin)
admin.site.register(Dessert, DessertAdmin)
admin.site.register(New, NewAdmin)
