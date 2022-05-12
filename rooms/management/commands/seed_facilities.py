from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    help = 'This commands tells me that he loves me'

    def add_arguments(self, parser):
        parser.add_argument(
            '--times',
            help='How many users do you want to create'
        )

    def handle(self, *args, **options):
        facilities  = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]

        for f in facilities :
            Facility.objects.create(name=f)

        self.stdout.write(self.style.SUCCESS('Facility created'))

    #     times = options.get('times')
    #         # self.stdout.write(self.style.SUCCESS('I love you'))
    #         # self.stdout.write(self.style.ERROR('I love you'))
    #         # self.stdout.write(self.style.WARNING('I love you'))
