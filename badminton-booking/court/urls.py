from django.urls import path
from court import views
from rest_framework.routers import DefaultRouter

app_name = 'court'
router = DefaultRouter()
router.register('court', views.CourtView, basename='addcourts')
router.register('booking-court', views.BookingView, basename='booking_court')
router.register('booking-list', views.BookingListView, basename='booking_list')

urlpatterns = [
    path("check-booking/", views.BookingExistView.as_view(), name='check_booking')
    # path("addcourt/", views.CourtView.as_view(), name='addcourt')
]
urlpatterns += router.urls

