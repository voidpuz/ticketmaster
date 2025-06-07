from django.db import models
from django.core.validators import MinValueValidator

from common.models import BaseModel


class Order(BaseModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    total_amount = models.IntegerField(validators=[MinValueValidator(0)])
    is_paid = models.BooleanField(default=False)