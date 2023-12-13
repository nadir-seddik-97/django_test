from django.urls import path

from .views import *


urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('register/', Register, name='register'),
    path('logout/', logout_view, name='logout'), 
    path("check_email_availability/", check_email_availability,name="check_email_availability"),
    path('home/', HomeListView.as_view(), name='home'),
    path('add_order/', add_order, name='add_order'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order'),
    path('update_order/<int:pk>/', update_order, name='update_order'),
    path('get_products/', get_products, name='get_products'),
    path('remove_order/<int:pk>/', remove_order, name='remove_order'),
    path('stores/', StoreListView.as_view(), name='all_store'),
    path('store_detail/<int:pk>/', StoreDetailView.as_view(), name='store_detail'),
    

]
