from rest_framework.serializers import ModelSerializer
from src.apps.customers.models import Customer


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'email')
