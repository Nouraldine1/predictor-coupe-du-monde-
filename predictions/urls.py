from django.urls import path
from . import views

app_name = 'predictions'
urlpatterns = [
    path('', views.dashboard_favoris, name='dashboard_favoris'), # Page 1 : Les Favoris du Futur
    path('confrontation/', views.match_predictor, name='match_predictor'), # Page 2 : Match Unique
    path('scenarios/', views.page_scenarios, name='page_scenarios'), # Page 3 : Mode Scénarios
]


