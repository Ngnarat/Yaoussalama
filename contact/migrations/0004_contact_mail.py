# Generated by Django 3.2.9 on 2021-12-26 13:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_contact_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='mail',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
    ]
