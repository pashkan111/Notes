from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import MultipleObjectsReturned
from django.db.models import Q, QuerySet
from apps.django_common.exceptions import ExistsUserError

class UserQueryset(QuerySet):
    def active(self):
        """Активный"""
        return self.filter(is_active=True)

    def staff(self):
        """Сотрудник"""
        return self.filter(is_staff=True)


class UserManager(BaseUserManager.from_queryset(UserQueryset)):
    def __create_user(
        self,
        mobile_phone: str,
        password: str,
        is_staff: bool = False,
        is_active: bool = False,
        is_superuser: bool = False,
    ):
        self.__check_user(mobile_phone)
        
        user = self.model(
            mobile_phone=mobile_phone,
            is_staff=is_staff,
            is_active=is_active,
            is_superuser=is_superuser,
        )
        user.set_password(password)

        user.save()
        return user

    def __check_user(self, mobile_phone: str) -> None:
        user_exists = self.model.objects.filter(
            mobile_phone=mobile_phone
            ).exists()
        if user_exists is True:
            raise ExistsUserError()

    def create_user(
        self, 
        mobile_phone: str, 
        password: str, 
        **kwargs
    ):
        return self.__create_user(
            mobile_phone,
            password,
            is_staff=kwargs.get("is_staff", False),
            is_active=kwargs.get("is_active", True),
            is_superuser=kwargs.get("is_superuser", False),
        )

    def create_superuser(self, mobile_phone: str, password: str):
        return self.__create_user(
            mobile_phone, 
            password,
            is_staff=True, 
            is_active=True, 
            is_superuser=True
            )

    def create(self, **kwargs):
        mobile_phone = kwargs.get("mobile_phone")
        if not mobile_phone:
            raise ValueError("Users must have a mobile phone")
        return self.create_user(**kwargs)

    def get_user(self, mobile_phone: str):
        try:
            return self.get(Q(**{self.model.USERNAME_FIELD: mobile_phone}))
        except MultipleObjectsReturned:
            return self.filter(Q(**{self.model.USERNAME_FIELD: mobile_phone})).last()
