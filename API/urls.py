from rest_framework.routers import DefaultRouter
from API.views import *
from django.urls import path, include

router = DefaultRouter()
router.register(r'User', User_Views)
router.register(r'Movie', Movie_Views)
router.register(r'Theater', Theater_Views)
router.register(r'Location', Location_Views)
router.register(r'ShowTime', ShowTime_Views)
router.register(r'Ticket', Ticket_Views)
router.register(r'Seat', Seat_Views)

urlpatterns = [
    path('', include(router.urls))
]