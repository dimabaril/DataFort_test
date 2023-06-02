from django.core.management.base import BaseCommand

from collector.services import collect_cities


class Command(BaseCommand):
    help = "Collects cities to the database"

    def handle(self, *args, **options):
        collect_cities()
        self.stdout.write(self.style.SUCCESS("Cities collected successfully"))
