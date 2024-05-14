from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    context = {'name': 'vasia', 'lastname': 'ivanov', 'age': 27}
    return render(request, template_name='home_workapp/index.html', context=context)


def home(request):
    return render(request, template_name='home_workapp/home.html')


