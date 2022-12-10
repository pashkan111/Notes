from rest_framework.renderers import JSONRenderer as BaseJSONRenderer

from . import handlers


def get_handler_class_by_status_code(status_code: str):
    if status_code.startswith('2'):
        return handlers.Handle200

    return getattr(handlers, f'Handle{status_code}', None)


def execute_handler_class(status_code: str, data: dict):
    handler_class = get_handler_class_by_status_code(status_code)

    if handler_class is None:
        return data

    handler = handler_class(raw_data=data)

    return handler()



class JSONRenderer(BaseJSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        data = execute_handler_class(
            status_code=str(renderer_context['response'].status_code), 
            data=data
            )
        return super().render(data, accepted_media_type, renderer_context)
