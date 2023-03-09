from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from core.filters import CustomFilter
from core.permissions import IsAdmin, IsAdminAccess
from court import serializers
from court.models import Court, Booking


# Create your views here.


class CourtView(viewsets.ModelViewSet):
    permission_classes = (IsAdmin,)
    queryset = Court.objects.all()
    serializer_class = serializers.CourtSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = serializers.ReadCourtSerializer(page, many=True, context={"request": request})
            return self.get_paginated_response(serializer.data)

        serializer = serializers.ReadCourtSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class BookingView(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = serializers.BookingSerializers
    filter_backends = (CustomFilter,)
    custom_filter_fields = {"user": "user_id"}

    def list(self, request, *args, **kwargs):
        # queryset = self.get_queryset().filter(user=request.query_params.get('user'))
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True, context={"request": request})
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True, context={"request": request})
        return Response({"data": serializer.data})


class BookingExistView(APIView):
    serializers_class = serializers.BookingExistSerializers

    def post(self, request):
        serializer = self.serializers_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        date = serializer.validated_data.get('date')
        court = serializer.validated_data.get('court')
        bookings = Booking.objects.filter(court_id=court, date=date).exists()
        if bookings:
            lis = []
            for i in Booking.objects.filter(court_id=court, date=date):
                lis += i.timeslot
            # data = [lis + i.timeslot for i in Booking.objects.filter(court_id=court, date=date)]
            data = list(set(lis))
            return Response({"data": data}, )
        else:   
            return Response({"message": "this  slot is available"})


class BookingListView(mixins.ListModelMixin, GenericViewSet):
    permission_classes = (IsAdminAccess,)
    queryset = Booking.objects.all()
    serializer_class = serializers.ReadBookingSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({"data": serializer.data})
