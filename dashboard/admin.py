from django.contrib import admin
from .models import Product, Customer, Invoice, InvoiceItem

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'status', 'product_code', 'amount_sold', 'quantity_sold', 'date_created']

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['total_amount', 'total_quantity', 'status', 'date_created']
    search_fields = ['date_created']

admin.site.register(Product, ProductAdmin)
admin.site.register(Customer)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceItem)
