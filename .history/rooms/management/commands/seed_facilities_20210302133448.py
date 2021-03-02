from django.core.management.base import BaseCommand
from rooms import models as room_models


class Command(BaseCommand):
    help = "This command creates facilities"

    """
        def add_arguments(self, parser):
            parser.add_argument(
                "--times",
                help="How many times do you want me to tell you that I love you?",
            )
        """

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for a in facilities:
            room_models.Facility.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("facilities created!"))
