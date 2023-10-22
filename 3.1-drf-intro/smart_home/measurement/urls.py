from django.urls import path

from measurement.views import SensorCreateView, Smart_HomeView, MeasurementCreateView, SensorUpdateView, Sensor_InfoView

urlpatterns = [
	path('sensors/create/', SensorCreateView.as_view(), name='create_sensor'),
	path('sensors/', Smart_HomeView.as_view(), name='show_sensors'),
	path('measurement/', MeasurementCreateView.as_view(), name='make_measurement'),
	path('sensors/<pk>/update/', SensorUpdateView.as_view(), name='update_sensor'),
	path('sensors/<pk>/', Sensor_InfoView.as_view(), name='show_sensor'),
]
