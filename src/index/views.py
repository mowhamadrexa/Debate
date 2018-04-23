from django.shortcuts import render
from django.views.generic.list import ListView
from debate.models import Debate


# Create your views here.

class Index(ListView):
    model = Debate
    context_object_name = 'debates'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
