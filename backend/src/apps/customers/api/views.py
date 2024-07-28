from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from src.apps.customers.models import Customer

from .schemas import CustomerSerializer


class CustomerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for managing customer data.

    Provides endpoints to list and retrieve customers by ID.
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @swagger_auto_schema(operation_summary="List all customers", tags=['Customer Management'])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Retrieve a customer by ID", tags=['Customer Management'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
