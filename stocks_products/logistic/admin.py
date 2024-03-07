from django.contrib import admin

# Register your models here.
from .models import Product, Stock, StockProduct

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
        list_display = ['title', 'description']

class StockProductInLine(admin.TabularInline):
    model = StockProduct
    list_display = ['product', 'quantity', 'price']
    extra = 0


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
        list_display = ['name', 'address']
        inlines = [StockProductInLine, ]
