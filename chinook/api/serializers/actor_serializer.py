from api.models import Actors
from rest_framework.serializers import ModelSerializer


class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actors
        fields = '__all__'
