from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This commnad tells me that he loves me"
    print("hello")

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            help="How many times do you want me to tell you that I love you?",
        )
