from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.decorators import api_view

from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

#from project.permissions import IsOwnerOrReadOnly
from project.models import Activity, AgeGroup, Information, Calendar
from project.serializers import InformationSerializer, ActivitySerializer, AgeGroupSerializer, CalendarSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        #'users': reverse('user-list', request=request, format=format),
        'calendars': reverse('calendars-list', request=request, format=format),
        'activities': reverse('activity-list', request=request, format=format),   
    })

class CalendarViewSet(viewsets.ModelViewSet):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """This viewset automatically provides `list`, `create`, `retrieve`, update` and `destroy` actions."""
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    #def perform_create(self, serializer):
    #    serializer.save(owner=self.request.user)


class AgeGroupViewSet(viewsets.ModelViewSet):
    queryset = AgeGroup.objects.all()
    serializer_class = AgeGroupSerializer


class InformationViewSet(viewsets.ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer



