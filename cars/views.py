from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Car
from .serializers import CarSerializer


class CarListAPIView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get("category")
        print(category)
        if category:
            return queryset.filter(category=category)
        return queryset

class CarRetrieveAPIView(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarArchiveListAPIView(ListAPIView):
    queryset = Car.objects.filter(status=Car.PASSED)
    serializer_class = CarSerializer