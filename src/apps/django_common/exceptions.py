from rest_framework import exceptions


class ExistsUserError(exceptions.APIException):
    status_code = 409
    default_code = "USER_EXISTS"
    default_detail = "User with such credentials already exists"
