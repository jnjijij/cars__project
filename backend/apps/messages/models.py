from django.contrib.auth import get_user_model
from django.db import models

from backend.core import BaseModel

from backend.apps.all_users import UserModel as User

UserModel: User = get_user_model()


class SendMessagesModel(BaseModel):
    class Meta:
        db_table = 'send_messages'
    sender = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    receiver = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.TextField()
