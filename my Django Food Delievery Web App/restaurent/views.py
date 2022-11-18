from django.shortcuts import render
from .models import *
from django.views import View
from django.utils.timezone import datetime
from customer.models import *
from django.contrib.auth.mixins import UserPassesTestMixin , LoginRequiredMixin

class Dashboard(  LoginRequiredMixin, UserPassesTestMixin,):
        def get(self,request):
            today = datetime.today()
            # print(today ,       today.year , today.month , today.day ,         today.date())
            #2022-11-06 18:47:39.620456    2022 11 6       2022-11-06

#sale of the day
            orders = OrderModel.objects.filter(created_on__month  = today.month )
            # orders = OrderModel.objects.filter(created_on__year  = today.year ,created_on__month  = today.month , created_on__day  = today.day  )
            # orders = OrderModel.objects.filter(created_on__date  = today.date()  )

            # #loop through the orders and add the price value
            total_revenue = 0 
            for order in orders :
                total_revenue += order.price

            context = {
                'orders' : orders , 
                'total_revenue' : total_revenue , 
                'total_orders' : len(orders)
            }
            # print(context)

            return render(request , 'restaurent/dashboard.html' , context)

        def test_func(self) :
             return self.request.user.groups.filter(name = 'Staff' ).exists()
    



class OrderDetails(UserPassesTestMixin , LoginRequiredMixin , View):
    def get(self , request , pk ):
            return render(request , 'restaurent/order-details.html' , {'order' : OrderModel.objects.get(pk= pk) })

    def post(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)
        order.is_shipped = True
        order.save()

        context = {
            'order': order
        }

        return render(request, 'restaurant/order-details.html', context)


    def test_func(self) :
             return self.request.user.groups.filter(name = 'Staff' ).exists()
    




class Dashboard(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        # get the current date
        today = datetime.today()
        orders = OrderModel.objects.filter(
            created_on__year=today.year, created_on__month=today.month, created_on__day=today.day)

        # loop through the orders and add the price value, check if order is not shipped
        unshipped_orders = []
        total_revenue = 0
        for order in orders:
            total_revenue += order.price

            if not order.is_shipped:
                unshipped_orders.append(order)

        # pass total number of orders and total revenue into template
        context = {
            'orders': unshipped_orders,
            'total_revenue': total_revenue,
            'total_orders': len(orders)
        }

        return render(request, 'restaurant/dashboard.html', context)

    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()
