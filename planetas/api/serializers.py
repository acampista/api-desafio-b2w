from rest_framework.serializers import ModelSerializer
from planetas.models import Planeta

class PlanetaSerializer(ModelSerializer):
    class Meta:
        model = Planeta
        fields = ('id', 'id_swapi', 'nome', 'clima', 'terreno', 'QtdAparicoes')