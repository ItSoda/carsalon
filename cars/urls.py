from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "car"

urlpatterns = [
    path("car/list/", views.CarListAPIView.as_view(), name="car-list"),
    path("car-archive/list/", views.CarArchiveListAPIView.as_view(), name="car-archive-list"),
    path("car/<int:pk>/", views.CarRetrieveAPIView.as_view(), name="car-retrieve"),
]