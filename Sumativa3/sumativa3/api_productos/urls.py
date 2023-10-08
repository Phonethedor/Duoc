from django.urls import path
from .views import *
from .viewsLogin import login

urlpatterns = [
    path('v1', lista_productos),
    path('login', login, name="login"),
]