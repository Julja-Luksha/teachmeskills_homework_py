from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from events.models import Event
from events.api.serializers import EventListSerializer, EventSerializer, UserShortSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.auth.models import User

class EventListView(APIView):
    @swagger_auto_schema(
        tags=["Events"],
        operation_description="List future events",
        responses={200: EventSerializer(many=True)}
    )
    def get(self, request):
        now = timezone.now()
        events = Event.objects.filter(meeting_time__gt=now)
        serializer = EventListSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


"""
class EventDetailView(APIView):
    def get(self, request, event_id):
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EventSerializer(event)
        return Response(serializer.data, status=status.HTTP_200_OK)
"""


class JoinEventView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["Events"],
        operation_description="Subscribe to the event",
        manual_parameters=[
            openapi.Parameter(
                "event_id",
                openapi.IN_PATH,
                description="ID event",
                type=openapi.TYPE_INTEGER
            )
        ],
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "message": openapi.Schema(type=openapi.TYPE_STRING)
                }
            ),
            400: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "error": openapi.Schema(type=openapi.TYPE_STRING)
                }
            ),
            404: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "error": openapi.Schema(type=openapi.TYPE_STRING)
                }
            ),
        }
    )
    def post(self, request, event_id):
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)
        if event.meeting_time <= timezone.now():
            return Response({"error": "Event already started"}, status=status.HTTP_400_BAD_REQUEST)
        user = request.user

        if event.users.filter(id=user.id).exists():
            return Response({"message": "Already joined"}, status=status.HTTP_200_OK)

        event.users.add(user)
        return Response({"message": "Joined successfully"}, status=status.HTTP_200_OK)


class MyEventsView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["Events"],
        operation_description="List of events the user is subscribed to",
        responses={200: EventSerializer(many=True)}
    )

    def get(self, request):
        user = request.user
        events = user.events.all()  # related_name="events" в модели Event
        serializer = EventListSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateEventView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["Events"],
        operation_description="Create a new event",
        request_body=EventSerializer,
        responses={201: EventSerializer}
    )
    def post(self, request):
        serializer = EventSerializer(data=request.data)

        if serializer.is_valid():
            event = serializer.save()
            return Response(EventSerializer(event).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersListView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=["Users"],
        operation_description="List all users (only admins)",
        responses={200: UserShortSerializer(many=True)}
    )
    def get(self, request):
        users = User.objects.all()
        serializer = UserShortSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
