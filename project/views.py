from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.decorators import api_view

from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

#from project.permissions import IsOwnerOrReadOnly
from project.models import Activity, ActivityMonth, Icon, Calendar
from project.serializers import IconSerializer, ActivitySerializer, ActivityMonthSerializer, CalendarSerializer


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

class ActivityMonthViewSet(viewsets.ModelViewSet):
    queryset = ActivityMonth.objects.all()
    serializer_class = ActivityMonthSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """This viewset automatically provides `list`, `create`, `retrieve`, update` and `destroy` actions."""
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class IconViewSet(viewsets.ModelViewSet):
    queryset = Icon.objects.all()
    serializer_class = IconSerializer



