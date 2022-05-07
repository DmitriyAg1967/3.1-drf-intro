from rest_framework import generics
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorInfoSerializer
from rest_framework.generics import get_object_or_404


class SensorList(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def sensor_list(self, serializer):
        sens = get_object_or_404(Sensor)
        return serializer.save(sens=sens)


class SensorUpdate(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementCreate(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def measurement_create(self, serializer):
        measur = get_object_or_404(Measurement)
        return serializer.save(measur=measur)

class MeasurementUpdate(generics.RetrieveUpdateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class SensorInfo(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all().prefetch_related('measured')
    serializer_class = SensorInfoSerializer



