from rest_framework_nested import routers
from django.conf.urls import url, include
from project.views import MonthViewSet, ActivityViewSet, CalendarViewSet, InformationViewSet, IconViewSet


#Grandparent
calendars_router = routers.SimpleRouter()
calendars_router.register('calendars', CalendarViewSet, basename='calendars')
#Parent
months_router = routers.NestedSimpleRouter(calendars_router, r'calendars', lookup='calendar')
months_router.register(r'months', MonthViewSet, basename='months')
# Child1= activities
activities_router = routers.NestedSimpleRouter(months_router, r'months', lookup='month')
activities_router.register(r'activities', ActivityViewSet, basename='activities')
# Child2= information
informations_router = routers.NestedSimpleRouter(months_router, r'months', lookup='month')
informations_router.register(r'informations', InformationViewSet, basename='informations')
# Child3= icons
icons_router = routers.NestedSimpleRouter(months_router, r'months', lookup='month')
icons_router.register(r'icons', IconViewSet, basename='icons')



urlpatterns = [
    url(r'^', include(calendars_router.urls)),
    url(r'^', include(months_router.urls)),
    url(r'^', include(activities_router.urls)),
    url(r'^', include(informations_router.urls)),
    url(r'^', include(icons_router.urls)),
]