from django.contrib import admin
from .models import *
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ("id",)


admin.site.register(MenuItem)
admin.site.register(Category) 
admin.site.register(OrderModel , OrderAdmin)