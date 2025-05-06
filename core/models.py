from django.db import models

class Contact(models.Model):
    LANDLORD = 'Landlord'
    TENANT = 'Tenant'
    CONTACT_TYPES = [(LANDLORD, 'Landlord'), (TENANT, 'Tenant')]

    name = models.CharField(max_length=255)
    contact_type = models.CharField(max_length=10, choices=CONTACT_TYPES)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.contact_type})"


class Unit(models.Model):
    unit_number = models.CharField(max_length=10)
    unit_type = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('Vacant', 'Vacant'), ('Occupied', 'Occupied')])
    owner = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='units')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Unit {self.unit_number} - {self.status}"


class Lease(models.Model):
    unit = models.OneToOneField(Unit, on_delete=models.CASCADE, related_name='lease')
    tenant = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='leases_as_tenant')
    landlord = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='leases_as_landlord')
    start_date = models.DateField()
    duration = models.IntegerField(help_text='Duration in months')
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_frequency = models.CharField(max_length=20, choices=[('Monthly', 'Monthly'), ('Yearly', 'Yearly')])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Lease for {self.unit} to {self.tenant.name}"
