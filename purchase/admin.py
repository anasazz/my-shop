from django.contrib import admin
from .models import Purchase,ProductInOutDBView


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['number', 'date', 'product', 'quantity', 'price', 'value']
    list_display_links = ['number']
    list_filter = ['product', 'date']
    search_fields = ['number', 'product__name']
    date_hierarchy = 'date'
    fields = ['number', 'date', 'product', 'quantity', 'price', 'value']
    readonly_fields = ['value']


admin.site.register(Purchase, PurchaseAdmin)
# admin.site.register(ProductInOutDBView)

