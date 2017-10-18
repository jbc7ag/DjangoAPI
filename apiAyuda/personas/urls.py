from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'(?P<pk>[0-9]+)/$', PersonaApi.as_view(), name="persona_endpoint"),
    url(r'^$', PersonasApi.as_view(), name="personas_endpoint")

]