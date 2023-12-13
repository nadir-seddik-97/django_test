import json
from django.http import JsonResponse
from django.views.generic import ListView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render,get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from ..models import *
from ..forms import OrderForm

class HomeListView(LoginRequiredMixin,ListView):
    model = Order
    template_name = 'home.html' 
    paginate_by = 10


    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        queryset=Order.objects.filter(user=self.request.user).order_by('-order_date')
        return queryset
    

@login_required
def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        # check if the form is valid 
        if form.is_valid():
            quantities = request.POST.get('quantities')
            # check if there is products selected  
            if json.loads(quantities):
               store = form.cleaned_data['store']
               user_id = request.user.id  

               # reate an order instance
               order = Order.objects.create(store_id=store.id, user_id=user_id)
               # initiliaze the total amount to 0
               total_amount = 0  

               
               # convert json string to dict
               quantities_dict = json.loads(quantities)  
            
               for product_id, quantity in quantities_dict.items():
                  product = Product.objects.get(pk=product_id)
                  # calculate total for each item
                  item_total = product.price * int(quantity)  
                  # calculate total amount from the items total and create an item instance 
                  total_amount += item_total  
                  Item.objects.create(order=order, product=product, quantity=quantity)

               order.total_amount= total_amount
               order.save()

               # redirect after creating the order
               return redirect('home')  
            else:
                 # redirect to add_order page and show a warning message
                 messages.warning(request, "No products were selected")
                 return redirect('add_order') 

    else:
        form = OrderForm()

    return render(request, 'add_order.html', {'form': form})

class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'order_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.user == self.request.user:
            return super().get(request, *args, **kwargs)
        else:
            
            return HttpResponseRedirect(reverse('login'))  


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = self.get_object()  
        context["items"] = Item.objects.filter(order=order)
        return context
@login_required
def update_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    form = OrderForm(instance=order)
    if(order.user != request.user):
        # redirect to login page
        return HttpResponseRedirect(reverse('login'))  


    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()

            # update quantities for existing items
            existing_quantities = request.POST.getlist('existing_quantities')
            item_ids = request.POST.getlist('item_ids')
            for item_id, quantity in zip(item_ids, existing_quantities):
                item = Item.objects.get(pk=item_id)
                item.quantity = quantity
                item.save()

            # create new items with quantities
            new_products = request.POST.getlist('new_products')
            new_quantities =json.loads(request.POST['new_quantities_list'])
            for product_id, quantity in zip(new_products, new_quantities):
                product = Product.objects.get(pk=product_id)
                Item.objects.create(order=order, product=product, quantity=quantity)

            # calculate and update the total amount for the order
            order.total_amount = sum(item.product.price * item.quantity for item in order.items.all())
            order.save()
             # redirect to home page
            return redirect('home') 
            

    context = {'form': form, 'order': order}
    return render(request, 'update_order.html', context)


def get_products(request):
    store_id = request.GET.get('store_id')
    products = Product.objects.filter(store_id=store_id)
    serialized_products = []
    for product in products:
        serialized_product = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'photo':product.photo.url
        }
        serialized_products.append(serialized_product)
 
    return JsonResponse({'products': serialized_products})
@login_required
def remove_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if(order.user != request.user):
        # Redirect to login page
        return HttpResponseRedirect(reverse('login'))  

    order.delete()

   
    messages.success(request, "Order Deleted successfully")
    return redirect('home')