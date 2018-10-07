from django.views.generic import ListView
from personas.models import Persona

# Create your views here.
class PersonaListView(ListView):
    model = Persona