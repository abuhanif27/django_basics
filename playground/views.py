from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def say_hello(request):
    numbers = [_ for _ in range(1, 11)]
    return render(request, 'hello.html', context={'numbers': numbers})
