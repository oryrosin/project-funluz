from rest_framework_nested import routers
from django.conf.urls import url, include
from project.views import CalendarViewSet, ActivityViewSet, ClientViewSet, ActivityMonthViewSet, IconViewSet


#Grandparent
clients_router = routers.SimpleRouter()
clients_router.register('clients', ClientViewSet, basename='clients')
#Parent
calendars_router = routers.NestedSimpleRouter(clients_router, r'clients', lookup='client')
calendars_router.register(r'calendars', CalendarViewSet, basename='calendars')
# Child1= activities
activities_router = routers.NestedSimpleRouter(calendars_router, r'calendars', lookup='calendar')
activities_router.register(r'activities', ActivityViewSet, basename='activities')
# Child2= activitymonths
activity_months_router = routers.NestedSimpleRouter(calendars_router, r'calendars', lookup='calendar')
activity_months_router.register(r'activity_months', ActivityMonthViewSet, basename='activity_months')
# Child3= icons
icons_router = routers.NestedSimpleRouter(calendars_router, r'calendars', lookup='calendar')
icons_router.register(r'icons', IconViewSet, basename='icons')



urlpatterns = [
    url(r'^', include(clients_router.urls)),
    url(r'^', include(calendars_router.urls)),
    url(r'^', include(activities_router.urls)),
    url(r'^', include(activity_months_router.urls)),
    url(r'^', include(icons_router.urls)),
]