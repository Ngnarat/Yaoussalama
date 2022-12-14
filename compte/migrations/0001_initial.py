# Generated by Django 3.2.9 on 2021-11-18 20:49

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=150, unique=True, verbose_name='Matricule')),
                ('first_name', models.CharField(max_length=150, verbose_name='Nom')),
                ('last_name', models.CharField(max_length=150, verbose_name='Prenom')),
                ('telephone', models.BigIntegerField(verbose_name='Telephone')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Mail')),
                ('dateOfBirth', models.DateField(verbose_name='Date de naissance')),
                ('photo', models.ImageField(blank=True, upload_to='profil')),
                ('adresse1', models.CharField(max_length=50, verbose_name='Adresse 1')),
                ('adresse2', models.CharField(blank=True, max_length=50, verbose_name='Adresse 2')),
                ('codePostal', models.IntegerField(verbose_name='Code postal')),
                ('ville', models.CharField(max_length=35, verbose_name='Ville')),
                ('country', models.CharField(max_length=15, verbose_name='Pays')),
                ('action', models.CharField(choices=[('RAS', '?? jour'), ('Relancer', '?? relancer'), ('Suspendre', '?? suspendre')], default='Relancer', max_length=15, verbose_name='Action')),
                ('dateLastPayment', models.DateField(blank=True, verbose_name=' Date dernier paiement')),
                ('sumLastPayment', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Somme pay??')),
                ('restToPay', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Reste ?? cotiser')),
                ('echeance', models.DateField(blank=True, verbose_name='Echeance de cotisation')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('regime', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='database.regime', verbose_name='Regime')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Montat')),
                ('date', models.DateField(auto_now_add=True)),
                ('commentaire', models.TextField(blank=True, max_length=500, verbose_name='Commentaire')),
                ('utilisateur', models.CharField(max_length=150)),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Beneficiaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('dateOfBirth', models.DateField()),
                ('photo', models.ImageField(upload_to='profil')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('lastUpdate', models.DateTimeField(auto_now=True)),
                ('LientFamilial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.lientfamilial', verbose_name='Lien de famille')),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Membre')),
            ],
        ),
    ]
