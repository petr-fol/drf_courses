from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="почта", help_text="укажите почту"
    )

    phone = models.CharField(
        max_length=35, verbose_name="телефон", help_text="укажите телефон", **NULLABLE
    )
    tg_nick = models.CharField(
        max_length=50, verbose_name="ник", help_text="укажите телеграм ник", **NULLABLE
    )
    avatar = models.ImageField(
        upload_to="users/avatars/", verbose_name="аватар", **NULLABLE
    )
    city = models.CharField(
        max_length=50, verbose_name="город", help_text="укажите город", **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
