import json
from django.http import JsonResponse
from django.views.generic import ListView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render,get_object_or_404, redirect
from ..models import *
from ..forms import OrderForm
class StoreListView(LoginRequiredMixin,ListView):
    model = Store
    template_name = 'store_all.html' 
    paginate_by = 10



class StoreDetailView(LoginRequiredMixin, ListView):
    model = Store
    template_name = 'store_detail.html'
    paginate_by = 10

    
    def get(self, request, *args, **kwargs):
        self.id = kwargs.get('pk')
        return super().get(request, *args, **kwargs)



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Store"]=Store.objects.get(pk=self.id)
        context["Products"] = Product.objects.filter(store=context["Store"])
        return context