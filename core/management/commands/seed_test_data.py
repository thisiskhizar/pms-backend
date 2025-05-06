from django.core.management.base import BaseCommand
from core.models import Contact, Unit, Lease
from datetime import date

class Command(BaseCommand):
    help = "Seed the database with test landlords, tenants, units, and leases."

    def handle(self, *args, **kwargs):
        if Contact.objects.exists():
            self.stdout.write(self.style.WARNING("Test data already exists. Aborting to avoid duplication."))
            return

        john = Contact.objects.create(name="John Doe", contact_type="Landlord", email="john@example.com", phone="1111111111")
        emma = Contact.objects.create(name="Emma Brown", contact_type="Landlord", email="emma@example.com", phone="2222222222")

        jane = Contact.objects.create(name="Jane Smith", contact_type="Tenant", email="jane@example.com", phone="3333333333")
        mark = Contact.objects.create(name="Mark Taylor", contact_type="Tenant", email="mark@example.com", phone="4444444444")

        unit1 = Unit.objects.create(unit_number="A1", unit_type="Apartment", location="City Center", value=1500.00, status="Occupied", owner=john)
        unit2 = Unit.objects.create(unit_number="B2", unit_type="Condo", location="Uptown", value=2000.00, status="Occupied", owner=emma)
        unit3 = Unit.objects.create(unit_number="C3", unit_type="Studio", location="Downtown", value=1200.00, status="Vacant", owner=john)

        Lease.objects.create(
            unit=unit1,
            tenant=jane,
            landlord=john,
            start_date=date(2025, 1, 1),
            duration=12,
            rent_amount=1500.00,
            payment_frequency="Monthly"
        )

        Lease.objects.create(
            unit=unit2,
            tenant=mark,
            landlord=emma,
            start_date=date(2025, 2, 15),
            duration=6,
            rent_amount=2000.00,
            payment_frequency="Monthly"
        )

        self.stdout.write(self.style.SUCCESS("Test data successfully created!"))
