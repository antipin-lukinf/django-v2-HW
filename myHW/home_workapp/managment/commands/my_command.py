from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Print 'Hello word!' to output"

    def handle(self, *args, **kwargs):
        self.stdout.write('Hello word!')
