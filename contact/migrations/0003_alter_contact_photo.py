# Generated by Django 3.2.9 on 2021-12-26 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_poste_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='photo',
            field=models.ImageField(blank=True, upload_to='contact/image'),
        ),
    ]
