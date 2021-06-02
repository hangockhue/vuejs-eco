from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Category, Product, Order, Highlight, HighlightBig
from rest_framework_simplejwt.tokens import RefreshToken,BlacklistMixin ,TokenError


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        data = super().get_token(user)
        data['username'] = user.username
        data['id'] = user.id
        return data
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['id'] = self.user.id
        return data

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            print(self.token)
            refresh = RefreshToken(self.token)
            refresh.blacklist()

        except TokenError:
            self.fail('bad_token')


class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'password')
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

    return user

# Login Serializer
class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()
  def validate(self, data):
    user = authenticate(**data)
    if user and user.is_active:
      return user
    raise serializers.ValidationError("Incorrect Credentials")

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("__all__")

class HighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Highlight
        fields = ("__all__")

class ProductSerializer(serializers.ModelSerializer):
    name_latin = serializers.ReadOnlyField()
    class Meta:
        model = Product
        fields = ("id","name", "price", "image", "category", "name_latin")
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("__all__")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "last_login")

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.set_password(validated_data.get('password', instance.password))
        instance.save()
        return instance
