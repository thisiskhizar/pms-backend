from rest_framework import viewsets
from .models import Contact, Unit, Lease
from .serializers import ContactSerializer, UnitSerializer, LeaseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count, Sum

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get_queryset(self):
        contact_type = self.request.query_params.get('type')
        if contact_type:
            return self.queryset.filter(contact_type=contact_type.capitalize())
        return self.queryset


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.select_related('owner').all()
    serializer_class = UnitSerializer


class LeaseViewSet(viewsets.ModelViewSet):
    queryset = Lease.objects.select_related('unit', 'tenant', 'landlord').all()
    serializer_class = LeaseSerializer

@api_view(['GET'])
def dashboard_view(request):
    total_units = Unit.objects.count()
    occupied_units = Unit.objects.filter(status='Occupied').count()
    vacant_units = Unit.objects.filter(status='Vacant').count()

    landlords = Contact.objects.filter(contact_type='Landlord').annotate(unit_count=Count('units')).values('name', 'unit_count')

    total_rent_income = Lease.objects.aggregate(total=Sum('rent_amount'))['total'] or 0

    test_lease = Lease.objects.first()
    lease_data = LeaseSerializer(test_lease).data if test_lease else {}

    return Response({
        'total_units': total_units,
        'occupied_units': occupied_units,
        'vacant_units': vacant_units,
        'landlords': list(landlords),
        'total_rent_income': total_rent_income,
        'test_lease': lease_data
    })


@api_view(['GET'])
def index_view(request):
    lease = Lease.objects.select_related('unit', 'tenant', 'landlord').first()
    if not lease:
        return Response({'message': 'No lease found. Please create test data.'})

    lease_data = LeaseSerializer(lease).data
    return Response({
        'summary': lease_data
    })