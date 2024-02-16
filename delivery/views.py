# delivery/views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .services import PriceCalculator

# class DeliveryCostCalculator(APIView):
#     def post(self, request):
#         zone = request.data.get('zone')
#         organization_id = request.data.get('organization_id')
#         total_distance = request.data.get('total_distance')
#         item_type = request.data.get('item_type')
        
#         if None in [zone, organization_id, total_distance, item_type]:
#             return Response({'error': 'Incomplete payload'}, status=400)
        
#         total_price = PriceCalculator.calculate_total_price(zone, organization_id, total_distance, item_type)
#         if total_price is None:
#             return Response({'error': 'Pricing not found for the given parameters'}, status=404)
        
#         return Response(total_price)

# delivery/views.py
# delivery/views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .services import PriceCalculator
# from .serializers import OrganizationSerializer, ItemSerializer, PricingSerializer


# class DeliveryCostCalculator(APIView):
#     def post(self, request):
#         serializer = PricingSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=400)

#         data = serializer.validated_data
#         zone = data.get('zone')
#         organization_id = data.get('organization_id')
#         total_distance = data.get('total_distance')
#         item_type = data.get('item_type')

#         total_price = PriceCalculator.calculate_total_price(zone, organization_id, total_distance, item_type)
#         if total_price is None:
#             return Response({'error': 'Pricing not found for the given parameters'}, status=404)
        
#         return Response(total_price)
# delivery/views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .services import PriceCalculator
# from .serializers import OrganizationSerializer, ItemSerializer, PricingSerializer

# class DeliveryCostCalculator(APIView):
#     def post(self, request):
#         serializer = PricingSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=400)

#         data = serializer.validated_data
#         zone = data.get('zone')
#         organization_id = data.get('organization_id')
#         total_distance = data.get('total_distance')
#         item_type = data.get('item_type')

#         total_price = PriceCalculator.calculate_total_price(zone, organization_id, total_distance, item_type)
#         if total_price is None:
#             return Response({'error': 'Pricing not found for the given parameters'}, status=404)
        
#         return Response(total_price)

# views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pricing, Organization, Item
from .services import PriceCalculator
from .serializers import OrganizationSerializer, ItemSerializer

@api_view(['POST'])
def calculate_delivery_cost(request):
    data = request.data
    organization_id = data.get('organization_id')
    total_distance = data.get('total_distance')
    item_type = data.get('item_type')

    try:
        organization = Organization.objects.get(id=organization_id)
        item = Item.objects.get(type=item_type)
    except Organization.DoesNotExist:
        return Response({"error": f"Organization with ID '{organization_id}' does not exist."}, status=400)
    except Item.DoesNotExist:
        return Response({"error": f"Item with type '{item_type}' does not exist."}, status=400)

    # total_price = PriceCalculator.calculate_total_price(organization, item, data['zone'], total_distance)
    total_price = PriceCalculator.calculate_total_price(data['zone'], organization_id, total_distance, item_type)


    return Response({"total_price": total_price})
