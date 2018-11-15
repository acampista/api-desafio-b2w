import request
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from planetas.models import Planeta
from .serializers import PlanetaSerializer

class PlanetaViewSet(ModelViewSet):
    queryset = Planeta.objects.all()
    serializer_class = PlanetaSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('id', 'id_swapi', 'nome')
    #permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        id_swapi = self.request.query_params.get('id_swapi', None)
        nome = self.request.query_params.get('nome', None)
        queryset = Planeta.objects.all()

        if id:
            queryset = Planeta.objects.filter(id=id)

        if id_swapi:
            queryset = Planeta.objects.filter(id_swapi=id_swapi)

        if nome:
            queryset = queryset.filter(nome__iexact=nome)

        return queryset

    #def list(self, request, *args, **kwargs):
    #    pass

    #def create(self, request, *args, **kwargs):
    #    pass

    #def destroy(self, request, *args, **kwargs):
    #    pass

    #def retrieve(self, request, *args, **kwargs):
    #    pass

    #def update(self, request, *args, **kwargs):
    #    pass

    #def partial_update(self, request, *args, **kwargs):
    #    pass