from graphene import relay

from graphene_django import DjangoObjectType

from events.models import Event


class ClubEventNode(DjangoObjectType):
    class Meta:
        model = Event
        fields = '__all__'
        interfaces = (relay.Node,)
