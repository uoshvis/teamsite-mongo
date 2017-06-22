from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers

from teamapp.models import Member, Team


class TeamSerializer(mongoserializers.DocumentSerializer):
    id = serializers.CharField(read_only=False)

    class Meta:
        model = Team
        fields = '__all__'


class MemberSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = Member
        fields = '__all__'
