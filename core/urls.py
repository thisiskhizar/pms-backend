from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet, UnitViewSet, LeaseViewSet, dashboard_view, index_view

router = DefaultRouter()
router.register(r'contacts', ContactViewSet)
router.register(r'units', UnitViewSet)
router.register(r'leases', LeaseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('index/', index_view, name='index'),
]
