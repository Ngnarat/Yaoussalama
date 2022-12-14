# Generated by Django 3.2.9 on 2021-11-21 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Param',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=15, unique=True, verbose_name='Clé')),
                ('value', models.CharField(max_length=25, verbose_name='Valeur')),
                ('description', models.TextField(max_length=500, verbose_name='déscription')),
                ('create_at', models.DateField(auto_now_add=True, verbose_name='Crée le')),
                ('update_at', models.DateField(auto_now=True, verbose_name='Modifier le')),
            ],
        ),
    ]
