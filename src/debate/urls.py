from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from .views import debate_index, new_comment

urlpatterns = [
    path('<int:pk>/', debate_index, name='debate'),
    path('<int:pk>/comment/', new_comment),
]
