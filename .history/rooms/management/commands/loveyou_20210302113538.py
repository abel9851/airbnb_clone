from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This commnad tells me that he loves me"
    print("hello")