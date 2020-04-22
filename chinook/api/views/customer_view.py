
from rest_framework.viewsets import ModelViewSet
from api.models import Customers
from  api.serializers import  CustomerSerializer


class CustomerViewset(ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer