from rest_framework.permissions import AllowAny
from .renderers import JSONRenderer


class PublicAPIView:
    permission_classes = [AllowAny]


class JSONResponseView:
    renderer_classes = [JSONRenderer]


class PublicJSONResponseView(PublicAPIView, JSONResponseView):
    pass
