from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response

from court.models import Court, Booking


class CourtSerializer(serializers.ModelSerializer):
    # image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Court
        fields = ['name', 'price', 'description', 'image']

    # def get_image_url(self, obj):
    #     return obj.image


class ReadCourtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Court
        fields = ['id', 'name', 'price', 'description', 'image']


class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def create(self, validated_data):
        booking_date = validated_data.get('date')
        booking_slot = validated_data.get('timeslot')
        validated_data['user'] = self.context.get('request').user
        if Booking.objects.filter(date=booking_date).exists():
            for slot in booking_slot:
                if Booking.objects.filter(timeslot=[slot]):
                    error = "{} this time slot is not available".format(slot)
                    return Response(error, status=status.HTTP_400_BAD_REQUEST)
                else:
                    data = Booking.objects.create(**validated_data)
                    return data
        else:
            data = Booking.objects.create(**validated_data)
            return data


class BookingExistSerializers(serializers.Serializer):
    date = serializers.DateField()
    court = serializers.IntegerField()


class ReadBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
