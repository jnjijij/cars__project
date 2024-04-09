from django.contrib.auth import get_user_model
from django.db import models

from backend.core import BaseModel

from backend.apps.all_users import ProfileModel
from backend.apps.all_users import UserModel as User

UserModel: User = get_user_model()
from backend.core import BaseModel


class ManagerModel(BaseModel):
    class Meta:
        db_table = 'manager'
        ordering = ('id',)

    # profile=models.OneToOneField(ProfileModel, on_delete=models.CASCADE, related_name='profile')
    # user=models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='auth_user')
    