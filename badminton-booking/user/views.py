from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.views import TokenViewBase
from core.permissions import IsAdminAccess
from user import serializers
from rest_framework import status, mixins
from user.models import User


class SignUpView(mixins.CreateModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = serializers.SignUpSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data={'success': "user created successfully"})


class LoginView(TokenViewBase):
    permission_classes = (AllowAny,)
    serializer_class = serializers.AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        access = serializer.validated_data['access']
        refresh = serializer.validated_data['refresh']
        data = {'access': access, 'refresh': refresh, 'user': user}
        return Response(data, status=status.HTTP_200_OK)


class UserListView(mixins.ListModelMixin, GenericViewSet):
    permission_classes = (IsAdminAccess,)
    queryset = User.objects.all()
    serializer_class = serializers.ReadUserSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({"data": serializer.data})