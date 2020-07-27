from rest_framework_nested import routers
from django.conf.urls import url, include
from project.views import CalendarViewSet, ActivityViewSet, OwnerViewSet, ActivityMonthViewSet, IconViewSet


#Grandparent
owners_router = routers.SimpleRouter()
owners_router.register('owners', OwnerViewSet, basename='owners')
#Parent
calendars_router = routers.NestedSimpleRouter(owners_router, r'owners', lookup='owner')
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
    url(r'^', include(owners_router.urls)),
    url(r'^', include(calendars_router.urls)),
    url(r'^', include(activities_router.urls)),
    url(r'^', include(activity_months_router.urls)),
    url(r'^', include(icons_router.urls)),
]