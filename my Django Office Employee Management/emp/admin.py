from django.contrib import admin
from .models import *

# class RoomAdmin(admin.ModelAdmin):
#     list_display = ('id' ,  'name' ,'get_online_count' )
    
# class MessageAdmin(admin.ModelAdmin):
#     list_display = ('id' ,  'get_user','get_room',  'content' , 'timestamp' )

# # Register your models here.
admin.site.register(Department )
admin.site.register(Role )
admin.site.register(Employee )
# admin.site.register(Message , MessageAdmin)