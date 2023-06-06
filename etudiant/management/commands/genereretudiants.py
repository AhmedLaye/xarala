from django.core.management.base import BaseCommand
from etudiant.models import Etudiant
import random
import string


class Command(BaseCommand):
    help = 'Génère 20 étudiants aléatoires'

    def handle(self, *args, **options):
        for _ in range(20):
            nom = ''.join(random.choices(string.ascii_uppercase, k=5))
            email = ''.join(random.choices(string.ascii_lowercase, k=5)) + '@example.com'
            phone = ''.join(random.choices(string.digits, k=10))
            status = random.choice(['actif', 'inactif'])

            etudiant = Etudiant(nom=nom, email=email, phone=phone, status=status)
            etudiant.save()

        self.stdout.write(self.style.SUCCESS('Les étudiants ont été générés avec succès.'))
