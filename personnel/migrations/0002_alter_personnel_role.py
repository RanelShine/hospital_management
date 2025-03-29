# Generated by Django 5.1.7 on 2025-03-29 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='role',
            field=models.CharField(choices=[('medecin', 'Médecin'), ('infirmier', 'Infirmier'), ('specialiste', 'Spécialiste')], default='medecin', max_length=50),
        ),
    ]
