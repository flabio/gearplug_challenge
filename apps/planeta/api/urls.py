from django.urls import path
from apps.planeta.api.views import PlanetList,PlanetDetail
urlpatterns = [
    path('list/',PlanetList.as_view(),name='planeta-list'),
    path('detail/<int:pk>',PlanetDetail.as_view(),name='planeta-detail'),
    
]
