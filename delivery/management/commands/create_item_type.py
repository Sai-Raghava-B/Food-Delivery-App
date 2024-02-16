from django.core.management.base import BaseCommand
from delivery.models import Item

class Command(BaseCommand):
    help = 'Create item types in the database'

    def add_arguments(self, parser):
        parser.add_argument('type', type=str, help='Type of the item')

    def handle(self, *args, **kwargs):
        item_type = kwargs['type']

        # Create item type
        item_type_obj, created = Item.objects.get_or_create(type=item_type)

        if created:
            self.stdout.write(self.style.SUCCESS(f'Item type "{item_type_obj.type}" created successfully'))
        else:
            self.stdout.write(self.style.WARNING(f'Item type "{item_type_obj.type}" already exists'))
