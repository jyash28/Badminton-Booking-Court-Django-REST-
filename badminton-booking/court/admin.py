from django.contrib import admin
from .models import Court, Booking

# Register your models here.


@admin.register(Court)
class CourtAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image', 'description')
    list_filter = ('name',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'court_id', 'date', 'timeslot', 'price')
    list_filter = ('price',)






