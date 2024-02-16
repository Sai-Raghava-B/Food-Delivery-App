from django.core.management.base import BaseCommand
from delivery.models import Organization

class Command(BaseCommand):
    help = 'Create organizations in the database'

    def add_arguments(self, parser):
        parser.add_argument('id', type=str, help='ID of the organization')
        parser.add_argument('name', type=str, help='Name of the organization')

    def handle(self, *args, **kwargs):
        org_id = kwargs['id']
        name = kwargs['name']

        # Check if organization already exists
        if Organization.objects.filter(id=org_id).exists():
            self.stdout.write(self.style.ERROR(f'Organization with ID "{org_id}" already exists'))
            return

        # Create organization
        organization = Organization.objects.create(id=org_id, name=name)

        self.stdout.write(self.style.SUCCESS(f'Organization "{organization.name}" with ID "{organization.id}" created successfully'))
