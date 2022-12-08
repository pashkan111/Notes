from django.contrib.auth import models as django_auth_models
from django.db import models
from . import managers


class User(
    django_auth_models.AbstractBaseUser, django_auth_models.PermissionsMixin
    ):
    created_at = models.DateTimeField(
        "Время создания", auto_now_add=True, db_index=True
        )
    mobile_phone = models.CharField(
        "MobilePhone", 
        unique=True, 
        max_length=11
        )
    is_staff = models.BooleanField("Is staff", default=False)
    is_superuser = models.BooleanField("Is is_superuser", default=False)
    is_active = models.BooleanField("Is active", default=True)

    USERNAME_FIELD = "mobile_phone"

    objects = managers.UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return str(self.mobile_phone)
