from functools import wraps
from django.shortcuts import get_object_or_404, redirect
from .models import Order

def owner_requires(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        order_id = kwargs.get('order_id')
        order = get_object_or_404(Order, pk=order_id)

        # Check if the logged-in user is the creator of the order
        if not request.user.is_authenticated or request.user != order.user:
            return redirect('login')  # Replace 'login' with the name/url of your login page
        
        return view_func(request, *args, **kwargs)
    
    return _wrapped_view
