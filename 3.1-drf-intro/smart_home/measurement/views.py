

from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView

from measurement.models import Sensor
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class Smart_HomeView(ListAPIView):
	queryset = Sensor.objects.all()
	serializer_class = SensorSerializer


class Sensor_InfoView(RetrieveAPIView):
	queryset = Sensor.objects.all()
	serializer_class = SensorDetailSerializer



class SensorCreateView(CreateAPIView):
	serializer_class = SensorSerializer


class MeasurementCreateView(CreateAPIView):
	serializer_class = MeasurementSerializer


class SensorUpdateView(UpdateAPIView):
	queryset = Sensor.objects.all()
	serializer_class = SensorSerializer