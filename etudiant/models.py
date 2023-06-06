from django.db import models
import random
import string


class Etudiant(models.Model):
    STATUT_CHOICES = (
        ('actif', 'Actif'),
        ('inactif', 'Inactif'),
    )
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=STATUT_CHOICES)

    @classmethod
    def generer_etudiants(cls):
        for _ in range(20):
            nom = ''.join(random.choices(string.ascii_uppercase, k=5))
            email = ''.join(random.choices(string.ascii_lowercase, k=5)) + '@example.com'
            phone = ''.join(random.choices(string.digits, k=10))
            status = random.choice(['actif', 'inactif'])

            etudiant = cls(nom=nom, email=email, phone=phone, status=status)
            etudiant.save()

    def __str__(self):
        return self.nom
