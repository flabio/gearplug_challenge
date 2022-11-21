
from django.urls import path
from apps.personaje.api.views import PersonajeList,PersonajeDetail



urlpatterns = [
  
    path('list/',PersonajeList.as_view(),name='personaje-list'),
    path('detail/<int:pk>',PersonajeDetail.as_view(),name='personaje-detail'),
    
]
