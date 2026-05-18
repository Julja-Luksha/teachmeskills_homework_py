from rest_framework import serializers
from django.contrib.auth.models import User
from events.models import Event
from dateutil import parser


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class EventListSerializer(serializers.ModelSerializer):
    users = UserShortSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ["id", "name", "meeting_time", "description", "users"]


class EventSerializer(serializers.ModelSerializer):
    users = UserShortSerializer(many=True, read_only=True)
    meeting_time = serializers.CharField()

    class Meta:
        model = Event
        fields = ["id", "name", "meeting_time", "description", "users"]

    def validate_meeting_time(self, value):
        try:
            dt = parser.parse(value)
        except Exception:
            raise serializers.ValidationError("I can't understand the date. Try this format '2026-06-01 18:00'.")
        return dt
