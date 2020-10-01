from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug':('name', )}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available', 'new')
    list_filter = ['available', 'new']
    list_editable = ('price', 'available', 'new')
    prepopulated_fields = {'slug':('name', )}

