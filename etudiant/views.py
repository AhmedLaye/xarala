from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from .models import Etudiant

def liste_etudiants(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'etudiants.html', {'etudiants': etudiants})

def modifier_etudiant(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, pk=etudiant_id)

    if request.method == 'POST':
        etudiant.nom = request.POST['nom']
        etudiant.email = request.POST['email']
        etudiant.phone = request.POST['phone']
        etudiant.status = request.POST['status']
        etudiant.save()
        return redirect('liste_etudiants')

    return render(request, 'modifier_etudiant.html', {'etudiant': etudiant})

def supprimer_etudiant(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, pk=etudiant_id)

    if request.method == 'POST':
        etudiant.delete()
        return redirect('liste_etudiants')

    return render(request, 'supprimer_etudiant.html', {'etudiant': etudiant})
