from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import login 
from django.shortcuts import render, redirect,HttpResponse

from ..forms import UserRegisterForm,LoginForm
from ..models import Users


def Register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "User Created Successfully")
            return redirect('login')  # Redirect to login page 
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'

def logout_view(request):
    logout(request)

@csrf_exempt
def check_email_availability(request):
    email = request.POST.get("email")
    try:
        user = Users.objects.filter(email=email).exists()
        if user:
            return HttpResponse(True)
        return HttpResponse(False)
    except Exception as e:
        return HttpResponse(False)


def handler404(request,exception):
    return render(request,'errors/404.html')
    

def handler500(request, *args, **argv):
    response = render('errors/500.html', {},context_instance=RequestContext(request))
    response.status_code = 500
    return response
