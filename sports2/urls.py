from sports2.views import *
from django.urls import path
app_name='sports2'
urlpatterns = [
    path('PTusha/',PTusha,name='PTusha'),
    path('PTushacareer/',PTushacareer,name='PTushacareer'),
]
