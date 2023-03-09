from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user.models import User


class SignUpSerializers(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"})

    class Meta:
        model = User
        fields = ['email', 'password', 'phone_number', 'gender']

    def create(self, validated_data):
        user = super(SignUpSerializers, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['id', 'email', 'phone_number', 'gender', ]
        fields = '__all__'


class AuthTokenSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['user'] = ReadUserSerializer(self.user).data
        return data


