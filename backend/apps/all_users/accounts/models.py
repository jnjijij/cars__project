from django.contrib.auth import get_user_model
from django.db import models

from backend.core import BaseModel

from backend.apps.all_users import PremiumSellerModel
from backend.apps.all_users.sellers import SellerModel
from backend.apps.all_users import UserModel as User

UserModel: User = get_user_model()


# from apps.all_users.users.models import UserModel


class AccountChoices(models.TextChoices):
    BASE_ACCOUNT = "base_account",
    PREMIUM_ACCOUNT = "premium_account"


class AccountOfOwnersModel(BaseModel):
    class Meta:
        db_table = 'accounts_of_owners'
        ordering = ('id',)

    base_account = models.OneToOneField(SellerModel, on_delete=models.CASCADE,
                                        choices=AccountChoices.choices, default='base_account')
    premium_account = models.OneToOneField(PremiumSellerModel, on_delete=models.CASCADE,
                                           choices=AccountChoices.choices, null=True, blank=True)
    owner = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='user', null=True, blank=True)
