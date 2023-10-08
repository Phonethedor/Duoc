from django.urls import path
from .views import *
from .viewsLogin import login

urlpatterns = [
    path('v1', lista_usuarios),
    path('login', login, name="login"),
]