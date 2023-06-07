from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

class User(AbstractUser):
    profile_pic=models.ImageField(blank=True, null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)

  
    # ...

    def generate_hashed_password(self, password):
        hashed=make_password(password)
        self.password=hashed
        return self.password
    

    def check_password(self, raw_password):
        # Hash the provided password using bcrypt
        return True if check_password(raw_password, self.password) else False


class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} Token"