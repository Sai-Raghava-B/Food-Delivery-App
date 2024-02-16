
from .models import Pricing
from decimal import Decimal


class PriceCalculator:
    @staticmethod
    def calculate_total_price(zone, organization_id, total_distance, item_type):
        
        pricing = Pricing.objects.filter(
            organization_id=organization_id,
            zone=zone,
            item__type=item_type
        ).first()

        if pricing is None:
            return None  

        # Calculate total price
        total_distance = Decimal(total_distance)
        base_price = pricing.base_price
        per_km_price = pricing.per_km_price_perishable
        per_km_price = pricing.per_km_price_non_perishable
        base_distance = pricing.base_distance

        if total_distance <= base_distance:
            total_price = base_price
        else:
            extra_distance = total_distance - base_distance
            per_km_price = pricing.per_km_price_perishable if item_type == 'Perishable' else pricing.per_km_price_non_perishable
            total_price = base_price + (extra_distance * per_km_price)

        return {'total_price': total_price}
