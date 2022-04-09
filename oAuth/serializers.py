from django.contrib.auth.models import User
from oAuth.models import NewUser
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ['url', 'username', 'email', 'is_staff']