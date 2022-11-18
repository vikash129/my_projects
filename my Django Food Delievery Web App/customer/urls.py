from django.urls import path 
from .views import *

urlpatterns = [
    path('', Index.as_view() , name='index'),
    path('menu/',Menu.as_view(), name='menu'),
    path('menu-search/',MenuSearch.as_view(), name='menu-search'),
    path('about/', About.as_view() , name='about'),
    path('order/', Order.as_view() , name='order'),
    path('order_confirmation/<int:pk>', OrderConfirmation.as_view() , name='order_confirmation'),
    path('payment_confirmation/', PaymentConfirmation.as_view() , name='payment_confirmation'),
]
