# chat/urls.py

from django.urls import path

from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('all_emp', All_Emp.as_view(), name='all_emp'),
    path('add_emp', Add_Emp.as_view(), name='add_emp'),
    path('remove_emp', Remove_Emp.as_view(), name='remove_emp'),
    path('remove_emp/<int:emp_id>',Remove_Emp.as_view() , name='remove_emp'),
    path('filter_emp', Filter_Emp.as_view(), name='filter_emp'),
]