from django.db import models

from backend.core import BaseModel


class CarDealershipModel(BaseModel):
    class Meta:
        db_table = 'car_dealership'

    name = models.CharField(max_length=20)
