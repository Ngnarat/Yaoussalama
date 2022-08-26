# Generated by Django 3.2.9 on 2021-12-29 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0008_rename_payment_payement'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isValidate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='lastVadidated',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='UserHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Crée le')),
                ('action', models.CharField(choices=[('Activer', 'Activer'), ('Désactiver', 'Désactiver')], max_length=50, verbose_name='Action')),
                ('utilisateur', models.CharField(choices=[('Activer', 'Activer'), ('Désactiver', 'Désactiver')], max_length=150, verbose_name='Enregistrer par')),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Menbre')),
            ],
        ),
    ]
