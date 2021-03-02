from django.core.management.base import BaseCommand
from django_seed import Seed
from users import models as users_models
from rooms import models as rooms_models


class Command(BaseCommand):
    help = "This command creates many rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="how many rooms do you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_user = users_models.User.objects.all()
        seeder.add_entity(
            rooms_models.Room,
            number,
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))
