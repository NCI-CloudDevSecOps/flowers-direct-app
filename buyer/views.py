from django.shortcuts import render, redirect
from django.views import View
from .models import FlowerItem, Category, OrderModel


class Index(View):
    # Renders the index.html template for the homepage.
    def get(self, request, *args, **kwargs):
        return render(request, 'buyer/index.html')


class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'buyer/about.html')


class Order(View):
    def get(self, request, *args, **kwargs):
        # Retrieves items for each category and passes them into the context.
        appetizers = FlowerItem.objects.filter(category__name__contains='Aster Flower')
        entres = FlowerItem.objects.filter(category__name__contains='Tulips')
        desserts = FlowerItem.objects.filter(category__name__contains='Delphiniums')
        drinks = FlowerItem.objects.filter(category__name__contains='Rose')

        # pass into context
        context = {
            'appetizers': appetizers,
            'entres': entres,
            'desserts': desserts,
            'drinks': drinks,
        }

        # render the template
        return render(request, 'buyer/order.html', context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        eir_code = request.POST.get('zip')

        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')
        # Retrieves selected items from the POST request and constructs order items.
        for item in items:
            menu_item = FlowerItem.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }

            order_items['items'].append(item_data)

            price = 0
            item_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        order = OrderModel.objects.create(
            price=price,
            name=name,
            email=email,
            street=street,
            city=city,
            state=state,
            eir_code=eir_code
        )
        order.items.add(*item_ids)

        # After everything is done, send confirmation email to the user
        body = ('Thank you for your order! Your food is being made and will be delivered soon!\n'
                f'Your total: {price}\n'
                'Thank you again for your order!')

        '''send_mail(
            'Thank You For Your Order!',
            body,
            'example@example.com',
            [email],
            fail_silently=False
        )'''

        context = {
            'items': order_items['items'],
            'price': price
        }

        return redirect('order-confirmation', pk=order.pk)
        
class OrderConfirmation(View):
    # Constructs the context for rendering the order confirmation page.
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)

        context = {
            'pk': order.pk,
            'items': order.items,
            'price': order.price,
        }

        return render(request, 'buyer/order_confirmation.html', context)
        
class OrderPayConfirmation(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'buyer/order_payment_confirmation.html')
        
class Menu(View):
    # Retrieves all flowers items.
    def get(self, request, *args, **kwargs):
        menu_items = FlowerItem.objects.all()

        context = {
            'menu_items': menu_items
        }

        return render(request, 'buyer/menu.html', context)
