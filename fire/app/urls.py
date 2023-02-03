from django.urls import path
from .views import *


urlpatterns = [
    path('s/<int:sport_id>/', sports, name='sports'),
]