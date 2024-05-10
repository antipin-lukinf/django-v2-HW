from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    html = """\
        <html>
          <head></head>
          <body>
          <a href="/">Главная</a>
            <p>
                Обо мне
            </p>
          </body>
        </html>
        """
    return HttpResponse(html)


def home(request):
    html_home = """\
        <html>
        <head></head>
        <body>
        <a href="/about/">О нас</a>
        
            <p>
                Главная страница
            </p>
        </body>
        </html>
        """
    return HttpResponse(html_home)
