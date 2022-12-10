from rest_framework import generics, permissions, renderers, request, response



class BaseFormView(generics.GenericAPIView):
    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)
    renderer_classes: tuple = (renderers.TemplateHTMLRenderer,)
    template_name: str

    def get(self, request: 'request.Request', *args, **kwargs):
        pass


from django.shortcuts import render


def register(request):
    return render(request, 'auth/register.html')


class RegisterView(BaseFormView):

    renderer_classes: tuple = (renderers.TemplateHTMLRenderer,)
    template_name = 'auth/register.html'

    def get(self, request: request.Request, *args, **kwargs):
        return response.Response()
