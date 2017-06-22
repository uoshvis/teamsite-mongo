from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet
from rest_framework.response import Response

from teamapp.serializers import TeamSerializer
from teamapp.models import Team


class TeamViewSet(MongoModelViewSet):

    lookup_field = 'id'
    serializer_class = TeamSerializer

    def get_queryset(self):
        return Team.objects.all()

    def list(self, request):
        queryset = Team.objects.all()
        serializer = TeamSerializer(queryset, many=True)
        data = serializer.data
        return Response(data)
