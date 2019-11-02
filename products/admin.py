from django.contrib import admin
from .models import Product


# ModelAdmin is a class contains all characteristics to do modification in admin object
# ProductAdmin class passes the ModelAdmin function
# list_display is we override attributes in the ModelAdmin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(Product, ProductAdmin)

