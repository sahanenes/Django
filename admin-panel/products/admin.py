from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "create_date", "is_in_stock", "update_date")
    list_editable = ( "is_in_stock", )
    # list_display_links = ("create_date", )
    list_filter = ("is_in_stock", "create_date")

admin.site.register(Product,ProductAdmin)

admin.site.site_title = "SAHAN"
admin.site.site_header = "SAHAN Admin Portal"  
admin.site.index_title = "Welcome to SAHAN Admin Portal"
