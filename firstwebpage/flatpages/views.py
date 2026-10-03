from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse(u'Привет, Мир!', content_type="text/plain")


def hello_default(request):
    # тип ответа не указан — Django подставит значение по умолчанию: text/html; charset=utf-8
    return HttpResponse(u'Привет, Мир!')


def index(request):
    return render(request, 'templates/index.html')


def home(request):
    return render(request, 'templates/static_handler.html')
