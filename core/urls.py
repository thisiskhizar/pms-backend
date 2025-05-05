from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet, UnitViewSet, LeaseViewSet

router = DefaultRouter()
router.register(r'contacts', ContactViewSet)
router.register(r'units', UnitViewSet)
router.register(r'leases', LeaseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
