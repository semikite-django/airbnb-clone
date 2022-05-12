from django.core.management.base import BaseCommand
from users.models import User
from django_seed import Seed

class Command(BaseCommand):

    help = 'This commands tells me that he loves me'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            default=2,
            type=int,
            help='How many users do you want to create'
        )

    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {
            'is_staff': False,
            'is_superuser': False,
        })
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f'{number} users created'))

    #     times = options.get('times')
    #         # self.stdout.write(self.style.SUCCESS('I love you'))
    #         # self.stdout.write(self.style.ERROR('I love you'))
    #         # self.stdout.write(self.style.WARNING('I love you'))
