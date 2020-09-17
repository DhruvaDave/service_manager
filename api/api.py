from rest_framework import viewsets, routers, serializers
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from .models import Entry
from .serializer import EntrySerializer

class EntryViewSet(viewsets.ModelViewSet):
    model = Entry
    serializer_class=EntrySerializer
    queryset = Entry.objects.all()

hours_router = routers.DefaultRouter()
hours_router.register('entry', EntryViewSet)