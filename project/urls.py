from django.urls import path, include
from rest_framework.routers import DefaultRouter
from project import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'activities', views.ActivityViewSet)
router.register(r'calendars', views.CalendarViewSet)
router.register(r'icons', views.IconViewSet)
router.register(r'activity_month', views.ActivityMonthViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]