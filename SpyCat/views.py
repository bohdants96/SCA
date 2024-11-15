from rest_framework import viewsets
from .models import SpyCat
from .serializer import SpyCatSerializer


class SpyCatViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing SpyCat instances.
    """
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer
