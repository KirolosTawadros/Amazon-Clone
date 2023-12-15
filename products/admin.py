from django.contrib import admin
from . models import Product,Brand,Review,ProductImages
# Register your models here.

class productImagesInline(admin.TabularInline):
    model = ProductImages


class ProductAdmin(admin.ModelAdmin):
    inlines = [productImagesInline]




admin.site.register(Product,ProductAdmin )
admin.site.register(Brand)
admin.site.register(Review)
