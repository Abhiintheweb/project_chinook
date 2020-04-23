
from rest_framework.viewsets import ModelViewSet
from api.models import Actors
from api.serializers import  ActorSerializer



class ActorViewset(ModelViewSet):

    queryset = Actors.objects.all()
    serializer_class = ActorSerializer