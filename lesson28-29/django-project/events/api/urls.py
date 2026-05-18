from django.urls import path
from events.api.auth import LoginView, RegisterView
from events.api.views import (EventListView, JoinEventView,
                              MyEventsView, CreateEventView, UsersListView)


urlpatterns = [
    path("events/", EventListView.as_view()),
    #path("events/<int:event_id>/", EventDetailView.as_view()),
    path("events/<int:event_id>/", JoinEventView.as_view()),
    path("events/my/", MyEventsView.as_view()),
    path("users/register/", RegisterView.as_view()),
    path("users/list/", UsersListView.as_view()),
    path("login/", LoginView.as_view()),
    path("events/create/", CreateEventView.as_view()),
]

