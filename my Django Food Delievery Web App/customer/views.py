from django.shortcuts import render , redirect
from django.views import View
from .models import *
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail

class Index(View):

    def get(self, request  ):
        print(request.user.is_authenticated)
        return render(request , 'customer/index.html' )

class About(View):
    def get(self, request):
        return render(request , 'customer/about.html')

class Order(View):
    def get(self, request ):
        
        context = { 
            'categories' :
             {
            'Desserts' :  MenuItem.objects.filter(category__name__contains  = 'Dessert') , 
            'Cakes' :  MenuItem.objects.filter(category__name__contains  = 'Cake') , 
            'Drinks' :  MenuItem.objects.filter(category__name__contains  = 'Drink') , 
            'Snacks' :  MenuItem.objects.filter(category__name__contains  = 'Snacks')
            }
        }
        
        return render(request , 'customer/order.html' , context)


    def post(self , request):

        items_id = list(map(int , request.POST.getlist('items')))

        name = request.POST.get('name')
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')

        total_price = 0
        order_items = []

        for item_id in items_id:
            menu_item = MenuItem.objects.get(pk__contains=item_id)
            total_price += menu_item.price
            order_items.append(menu_item)
        
        order = OrderModel.objects.create(
            price=total_price,
            name=name,
            email=email,
            street=street,
            city=city,
            state=state,
            zip_code=zip_code
            )

        # print(order_items) #[<MenuItem: app4>, <MenuItem: app5>]
        # print(*order_items) #app4 app5

        order.items.add(*order_items)
        print('order items ' , order)

        #send confirmation to the user
        
        # After everything is done, send confirmation email to the user
        body = (f'Thank {name} for your order! Your food is being made and will be delivered soon in : \n{street} , {city} , {state} , {zip_code} \n'
                f'Your total: {total_price}\n'
                'Thank you again for your order!')

        # print(body)

        
        try :
            send_mail(
            subject =  'Thank You For Your Order!',
            message =   body,
            from_email =  settings.EMAIL_HOST_USER,
            recipient_list =   [email],
            fail_silently=False
            )
            print('email sent')

        except:
            print('email not sent')


        return redirect( 'order_confirmation' , pk = order.pk)


class OrderConfirmation(View):
    def get(self, request, pk ,  *args, **kwargs):

        order = OrderModel.objects.get(pk = pk)



        context = {
            'pk': order.pk,
            'items': order.items.all(),
            'price': order.price,
            "name":order.name,
            "email":order.email,
        }
        return render(request, 'customer/order_confirmation.html' , context)

    def post(self , request):
        print("req.body" ,  request.body)
        return redirect('payment_confirmation' )



class PaymentConfirmation(View):
    def get(self, request,   *args, **kwargs):
        return render(request, 'customer/payment_confirmation.html' )

   

class Menu( View):
    def get(self , request ):
            return render(request , 'customer/menu.html' , {'items' : MenuItem.objects.all() })


class MenuSearch( View):
    def get(self , request):
            query = self.request.GET.get("q")

            menu_items = MenuItem.objects.filter(
                Q(name__icontains=query) |   Q(price__icontains=query) |    Q(description__icontains=query)
            )

            context = {
                'items': menu_items
            }

            return render(request, 'customer/menu.html', context)



