# delivery/management/commands/create_pricing_entries.py
from django.core.management.base import BaseCommand
from delivery.models import Organization, Item, Pricing

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Fetch the organization and item
        organization = Organization.objects.get(id="005")
        item = Item.objects.get(type="Perishable")
        
        # Create a Pricing entry with the specified values
        pricing = Pricing.objects.create(
            organization=organization,
            item=item,
            zone="central",
            base_price=10,  # Base price of 10 euros
            base_distance=5,  # Base distance of 5 km
            per_km_price_perishable=1.5,  # Per km price for perishable items
            per_km_price_non_perishable=1.0,  # Per km price for non-perishable items
        )
