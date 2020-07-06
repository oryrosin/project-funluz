from django.urls import path, include
from rest_framework.routers import DefaultRouter
from project import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'activities', views.ActivityViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'textmessage', views.TextMessageViewSet)
router.register(r'monthsubtitle', views.MonthSubtitleViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]