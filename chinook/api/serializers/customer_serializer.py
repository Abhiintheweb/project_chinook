
from api.models import Customers
from rest_framework.serializers import ModelSerializer


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'

