import random

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import RegistrationForm
from .models import Storage



class SignUp(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('my_rent')
    template_name = 'registration/signup.html'


def index(request):
    if request.method == "POST":
        user = authenticate(username=request.POST["EMAIL"], password=request.POST["PASSWORD"])
        print(user.client.phone)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(my_rent)
            else:
                # Return a 'disabled account' error message
                ...
        else:
            # Return an 'invalid login' error message.
            ...
        return redirect(index)

    random_storage = random.choice(Storage.objects.all())
    storage_box_count = random_storage.boxes.count()
    free_box_count = storage_box_count - random_storage.boxes.filter(is_rented=True).count()
    context = {
        'storage': random_storage,
        'box_count': storage_box_count,
        'free_box': free_box_count,
    }

    return render(request, 'index.html', context)


def boxes(request):
    context = {
        'storages': Storage.objects.all(),
    }
    return render(request, 'boxes.html', context)


def faq(request):
    return render(request, 'faq.html')


@login_required(login_url='/?login=1')
def my_rent(request):
    return render(request, 'my-rent.html')
