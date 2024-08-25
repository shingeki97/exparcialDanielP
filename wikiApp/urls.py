from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_principal, name='vista_principal'),
    path('nuevo_tema/', views.crear_nuevo_tema, name='crear_nuevo_tema'),
    path('nuevo_articulo/', views.crear_nuevo_articulo, name='crear_nuevo_articulo'),
    path('tema/<int:tema_id>/', views.articulos_por_tema, name='articulos_por_tema'),
    path('articulo/<int:articulo_id>/', views.vista_articulo, name='vista_articulo'),
    path('buscar/', views.vista_busqueda, name='vista_busqueda'),
]






