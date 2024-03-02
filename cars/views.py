from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Car
from .serializers import CarSerializer


class CarListAPIView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarRetrieveAPIView(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarArchiveListAPIView(ListAPIView):
    queryset = Car.objects.filter(status=Car.PASSED)
    serializer_class = CarSerializer