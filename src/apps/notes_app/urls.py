from django.urls import path
from . import views


urlpatterns = [
    path('main', views.main, name='main'),
    path('create-edit', views.create_edit, name='create-edit')
]
