# Generated by Django 3.2.9 on 2021-12-25 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-create_at'], 'verbose_name': 'Message'},
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(max_length=5000, verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sujet',
            field=models.CharField(max_length=150, verbose_name='Sujet'),
        ),
    ]
