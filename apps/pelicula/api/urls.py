from django.urls import path
from apps.pelicula.api.views import PeliculaList,PeliculaDetail
urlpatterns = [
    path('list/',PeliculaList.as_view(),name='pelicula-list'),
    path('detail/<int:pk>',PeliculaDetail.as_view(),name='pelicula-detail'),
    
]
