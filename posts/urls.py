from django.urls import path
from . import views
urlpatterns = [
    path(r'', views.index,name='index'), #Acá redirigirá al index.html
    path(r'base_layout',views.base_layout,name='base_layout'), #Y acá al base.html
]