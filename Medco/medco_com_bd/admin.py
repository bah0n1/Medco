from django.contrib import admin
from .models import (
    Customer,
    Product,
    Cart,
    Status,
)



@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=["id","user","locality","city"]


@admin.register(Product)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=["id","titel","generic_name","strength","manufactured_by","unit_price","pack_price"]




@admin.register(Cart)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=["id","user","product","quantity"]



@admin.register(Status)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=["id","user","customer","product","order_date","status"]