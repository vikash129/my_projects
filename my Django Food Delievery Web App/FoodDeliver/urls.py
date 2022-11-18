
from django.conf import settings
from django.contrib import admin
from django.urls import path , include 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('customer.urls')),
    path('restaurent/', include('restaurent.urls')),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)



# settings.MEDIA_URL = /media/ 
#  settings.MEDIA_ROOT =P:\Food Delievery Web App\media

# print("url " ,urlpatterns)
# url  [
#     <URLResolver <URLPattern list> (admin:admin) 'admin/'>,
#      <URLResolver <module 'customer.urls' from 'P:\\Food Delievery Web App\\customer\\urls.py'> (None:None) ''>,
#       <URLPattern '^media/(?P<path>.*)$'>]