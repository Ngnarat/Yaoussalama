# Generated by Django 3.2.9 on 2021-12-17 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0004_alter_payment_utilisateur'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiaire',
            name='isactive',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='beneficiaire',
            name='photo',
            field=models.ImageField(blank=True, upload_to='profil'),
        ),
    ]
