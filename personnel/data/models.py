from django.db import models

class Personnel(models.Model):
    ROLE_CHOICES = [
        ('medecin', 'Médecin'),
        ('infirmier', 'Infirmier'),
        ('specialiste', 'Spécialiste'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='medecin')
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.get_role_display()}"
