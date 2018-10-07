from django.conf.urls import url
from personas.views import PersonaListView
urlpatterns = [
    url(r'^$',PersonaListView.as_view())
]