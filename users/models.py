import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.models import nb
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None
    email = models.EmailField(verbose_name='Email:', unique=True)
    address = models.CharField(verbose_name='Адрес доставки', max_length=300)
    phone = models.PositiveBigIntegerField(verbose_name='Номер телефона', **nb)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email