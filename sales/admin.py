from django.contrib import admin

from .models import Client, Product, Sale
# from erp_framework.sites import erp_admin_site


# Register your models here.
admin.site.register(Client)

class ProductAdmin(admin.ModelAdmin):

    list_display = ["name", "available_quantity","average_price"]
admin.site.register(Product,ProductAdmin)


class SaleAdmin(admin.ModelAdmin):
    list_display = ["number", "date", "client", "product", "quantity", "price", "value"]
    list_display_links = ["number"]
    list_filter = ["client", "product", "date"]
    search_fields = ["number", "client__name", "product__name"]
    date_hierarchy = "date"
    fields = ["number", "date", "client", "product", "quantity", "price", "value"]
    readonly_fields = ["value"]


admin.site.register(Sale, SaleAdmin)
