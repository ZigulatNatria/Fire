from django.urls import path
from .views import *


urlpatterns = [
    path('<int:sport_id>/', sports, name='sports'),
    path('sport/', SportListView.as_view(), name='sport'),
    # path('sport/<int:pk>/', SportDetail.as_view(), name='detail_sport'),
]