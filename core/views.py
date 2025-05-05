from rest_framework import viewsets
from .models import Contact, Unit, Lease
from .serializers import ContactSerializer, UnitSerializer, LeaseSerializer

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
