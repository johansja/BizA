from django.contrib import admin

from .models import Uom, Product


class UomAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbreviation']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'uom']


admin.site.register(Uom, UomAdmin)
admin.site.register(Product, ProductAdmin)
