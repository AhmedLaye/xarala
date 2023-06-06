from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_etudiants, name='liste_etudiants'),
    path('etudiant/<int:etudiant_id>/modifier/', views.modifier_etudiant, name='modifier_etudiant'),
    path('etudiant/<int:etudiant_id>/supprimer/', views.supprimer_etudiant, name='supprimer_etudiant'),
]
