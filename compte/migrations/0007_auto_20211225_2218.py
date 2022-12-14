# Generated by Django 3.2.9 on 2021-12-25 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0006_rename_isactive_beneficiaire_isactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiaire',
            name='dateOfBirth',
            field=models.DateField(verbose_name='Date de naissance'),
        ),
        migrations.AlterField(
            model_name='beneficiaire',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Crée le'),
        ),
        migrations.AlterField(
            model_name='beneficiaire',
            name='first_name',
            field=models.CharField(max_length=150, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='beneficiaire',
            name='isActive',
            field=models.BooleanField(default=False, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='beneficiaire',
            name='lastUpdate',
            field=models.DateTimeField(auto_now=True, verbose_name='Modifier le'),
        ),
        migrations.AlterField(
            model_name='beneficiaire',
            name='last_name',
            field=models.CharField(max_length=150, verbose_name='Prenom'),
        ),
        migrations.AlterField(
            model_name='beneficiaire',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media/beneficiaire', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, upload_to='madia/profil'),
        ),
    ]
