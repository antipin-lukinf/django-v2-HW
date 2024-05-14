from django.core.management.base import BaseCommand


from home_workapp.models import *



name = input('Введите имя клиента: ')
email = input('Введите E-mail клиента: ')
age = input('Введите возраст клиента: ')


class Command(BaseCommand):
    help = 'Add user'

    def handle(self, *args, **kwargs):
        user = User(name=name, email=email, age=age)
        user.save()
        self.stdout.write(f'{user}')
