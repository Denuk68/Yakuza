from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug':('name', )}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category','name',  'price', 'available', 'new')
    list_display_links = ['name']
    list_filter = ['available', 'new','category']
    list_editable = ('price', 'available', 'new')
    prepopulated_fields = {'slug':('name', )}

