from django import forms
from ..models import Order
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['store'] 
        quantities = forms.IntegerField(min_value=1)

