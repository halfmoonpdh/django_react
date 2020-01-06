from rest_framework import serializers
from .models import DemoUser, Poster


class DemoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemoUser
        fields = '__all__'


class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = '__all__'
