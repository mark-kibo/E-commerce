from django.db import models
from users.models import User


# Create your models here.
class PaymentMethod(models.Model):
    payment_method_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=255, default="")
    account_number = models.CharField(max_length=255, default="")
    expiry_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
