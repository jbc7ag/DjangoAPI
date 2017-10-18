from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'/LugaresPersonas', LugareshasPersonaApi.as_view(),name="lugares_persona_endpoint"),
    url(r'^$', LugaresApi.as_view(),name="lugares_endpoint")
]