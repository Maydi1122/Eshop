from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import ListView
from .templates.forms import UserRegisterForm

from .models import profile
# Create your views here.
def login(request):
    context =locals()
    template ='accounts.html'
    return render(request,template,context)

class HomeView(ListView):
    template_name = 'home.html'
    model = profile

    



def about(request):
    context = locals()
    template='about.html'
    return render(request,template,context)

def register(request):
    if request.method == 'POST':

        form= UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,print('Account created for {}!'.format(username)))
            return redirect('home')
    else:

        form =UserRegisterForm()
    return render(request,'register.html',{'form':form})

def checkout(request):
    context = locals()
    template='checkout.html'
    return render(request,template,context)