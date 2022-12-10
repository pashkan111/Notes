from abc import ABC
from rest_framework.exceptions import ErrorDetail


handlers = {
    "NOT_FOUND": ("Not found", ""),
    "NOT_AUTHENTICATED": ("Not authenticated", ""),
    "INVALID_DATA": "Invalid input data",
}


class AbstractHandler(ABC):
    raise_default: bool = False
    is_successful: bool = False

    _error_code: str = None
    _error_message: str = None

    def __init__(self, raw_data: dict, **kwargs):
        self.raw_data = raw_data

    def error_detail(self) -> dict:
        if isinstance(self.raw_data, (tuple, list)):
            for raw_data in self.raw_data:
                self.raw_data = {'detail': raw_data}
                break
        if isinstance(self.raw_data.get('detail'), ErrorDetail) and not self.raise_default:
            self._error_code = self.raw_data['detail'].code
            self._error_message = str(self.raw_data['detail'])

        if not self._error_message or self._error_message == 'None':
            self._error_message = self.raw_data

        if (
            isinstance(self.raw_data.get('non_field_errors'), list)
            and len(self.raw_data['non_field_errors']) >= 1
            and isinstance(self.raw_data['non_field_errors'][0], ErrorDetail)
        ):
            self._error_message = f"{self._error_message}. {str(self.raw_data['non_field_errors'][0])}"

        return {'code': self._error_code, 'description': self._error_message}

    def __call__(self) -> dict:
        if self.is_successful:
            return {'data': self.raw_data, 'error': None}

        return {'data': None, 'error': self.error_detail()}


class Handle200(AbstractHandler):
    is_successful = True


class Handle400(AbstractHandler):
    _error_code = "INVALID_DATA"


class Handle401(AbstractHandler):
    _error_code = "NOT_AUTHENTICATED"
    raise_default = True


class Handle403(AbstractHandler):
    ...


class Handle404(AbstractHandler):
    _error_code = "NOT_FOUND"
    raise_default = False
