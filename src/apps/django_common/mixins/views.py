from rest_framework.permissions import AllowAny



class PublicAPIView:
    permission_classes = [AllowAny]


class JSONResponseView:
    pass


class PublicJSONResponseView(PublicAPIView, JSONResponseView):
    pass
