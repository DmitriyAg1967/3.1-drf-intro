from django.urls import path
from measurement.views import SensorList, SensorUpdate, MeasurementCreate, MeasurementUpdate, SensorInfo

urlpatterns = [
   path('sensorlist/', SensorList.as_view()),      # список всех датчиков с возможностью добавления новых
   path('sensorlist/<int:pk>', SensorUpdate.as_view()),     # страница редактирования выбранного по id датчика
   path('measurementcreate/', MeasurementCreate.as_view()),    # страница для добавления нового измерения
   path('measurementcreate/<int:pk>', MeasurementUpdate.as_view()),     # страница редактирования существующего измерения
   path('sensorinfo/<int:pk>', SensorInfo.as_view()),    # страница полной информации о датчике выбранном по id
]
