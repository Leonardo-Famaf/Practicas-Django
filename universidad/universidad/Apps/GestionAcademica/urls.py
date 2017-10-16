from django.conf.urls import url

from universidad.Apps.GestionAcademica.views import index_gestion

urlpatterns = [
    url(r'^index$', index_gestion),
]
