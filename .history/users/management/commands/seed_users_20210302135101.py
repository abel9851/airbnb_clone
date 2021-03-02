from django.core.management.base import BaseCommand
from django_seed import Seed
from rooms import models as room_models


class Command(BaseCommand):
    help = "This command creates many users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            help="how many users do you want to create",
        )

    def handle(self, *args, **options):

        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} facilities created!"))
