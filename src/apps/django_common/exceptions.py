from rest_framework import exceptions


class ExistsUserError(exceptions.APIException):
    status_code = 400
    default_code = "USER_EXISTS"
    default_detail = "User with such credentials already exists"


class NoActiveAccountError(exceptions.APIException):
    status_code = 400
    default_code = "NO_ACTIVE_ACCOUNT"
    default_detail = "User with such credentials not found"


class NoCategoryError(exceptions.APIException):
    status_code = 400
    default_code = "NO_CATEGORY"
    default_detail = "Category with this name does not exist"