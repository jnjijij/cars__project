from django.db import models

from backend.core import BaseModel

from backend.apps.cars_details import CarModelV2


class CarViewModel(BaseModel):
    class Meta:
        db_table = 'car_views'

    car_ad = models.OneToOneField(CarModelV2, on_delete=models.CASCADE, related_name='car_views')
    views = models.IntegerField(default=0)

