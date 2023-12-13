from django.test import TestCase, Client
from django.urls import reverse
from .models import *

class OrderDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = Users.objects.create_user(username='user', password='user')
        self.store = Store.objects.create(name="TestStore")
        self.product = Product.objects.create(store=self.store,name="test1",description="test11",price=100)
        self.order = Order.objects.create(user=self.user, store=self.store)  
        self.item = Item.objects.create(order=self.order,product=self.product,quantity=2)  

    def test_order_detail_view_authenticated_user(self):
        # login user
        self.client.login(username='user', password='user')
        url = reverse('order', kwargs={'pk': self.order.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200) # verify if he return 200
        self.assertTemplateUsed(response, 'order_detail.html') 
    def test_order_detail_view_unauthenticated_user(self):
        url = reverse('order', kwargs={'pk': self.order.pk})
        response = self.client.get(url)
        expected_redirect_url = reverse('login') + f'?next={url}' 
        self.assertRedirects(response, expected_redirect_url)    


class AddOrderViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        # create a store and a product in that store 
        self.store = Store.objects.create(name="TestStore") 
        self.product = Product.objects.create(store=self.store,name="TestProduct", price=50)  

    def test_add_order_with_products_selected(self):
        # login user
        self.client.login(username='user', password='user')

        # do a post request
        data = {
            'store':self.store, 
            'quantities': '{"' + str(self.product.id) + '": "2"}' 
        }
        response = self.client.post(reverse('add_order'), data)

        self.assertEqual(response.status_code, 302)  # verify if he return 302
        self.assertRedirects(response, reverse('home'))  
       

    def test_add_order_without_products_selected(self):
        # login user
        self.client.login(username='test', password='test')

         # do a post request
        data = {'store': self.store}  
        response = self.client.post(reverse('add_order'), data)

        self.assertEqual(response.status_code, 302)  # verify if he return 302
        
        self.assertRedirects(response, '/accounts/login/?next=/add_order/')

 



class UpdateOrderViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = Users.objects.create_user(username='user', password='user')
        self.client.login(username='user', password='user')

        # create a store and a product in that store and an order and order items
        self.store = Store.objects.create(name="TestStore")
        self.product = Product.objects.create(store=self.store, name="TestProduct", price=50)
        self.order = Order.objects.create(user=self.user, store=self.store)
        self.item = Item.objects.create(order=self.order, product=self.product, quantity=2)

    def test_update_order_authenticated_user(self):
        data = {
            'existing_quantities': [2],  
            'item_ids': [self.item.id], 
            'new_products': [6],  
            'new_quantities': [2]  
        }
        response = self.client.post(reverse('update_order', kwargs={'pk': self.order.pk}), data)
        self.assertEqual(response.status_code, 302)  # verify if he return 302
        self.assertRedirects(response, reverse('home'))  
       

    def test_update_order_unauthenticated_user(self):
         # logout user
        self.client.logout()  
        response = self.client.get(reverse('update_order', kwargs={'pk': self.order.pk}))
        self.assertEqual(response.status_code, 302) # verify if he return 302
        
        


class RemoveOrderViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        # create a user and  store and a product in that store and an order and order items
        self.user = Users.objects.create_user(username='test', password='test')
        self.client.login(username='test', password='test')
        self.store = Store.objects.create(name="TestStore")
        self.order = Order.objects.create(store=self.store,user=self.user)

    def test_remove_order_authenticated_user(self):
        response = self.client.post(reverse('remove_order', kwargs={'pk': self.order.pk}))
        self.assertEqual(response.status_code, 302)  # verify if he return 302
        self.assertFalse(Order.objects.filter(pk=self.order.pk).exists())  
     

    def test_remove_order_unauthenticated_user(self):
        # logout user
        self.client.logout()  
        response = self.client.post(reverse('remove_order', kwargs={'pk': self.order.pk}))
        self.assertEqual(response.status_code, 302) # verify if he return 302
        self.assertTrue(Order.objects.filter(pk=self.order.pk).exists())  