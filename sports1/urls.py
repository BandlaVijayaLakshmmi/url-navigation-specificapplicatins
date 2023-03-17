from sports1.views import *
from django.urls import path
app_name='sports1'
urlpatterns = [
    path('Himadas/',Himadas,name='Himadas'),
    path('Himadascareer/',Himadascareer,name='Himadascareer'),
]
