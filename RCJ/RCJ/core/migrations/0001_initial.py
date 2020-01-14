# Generated by Django 3.0.1 on 2020-01-10 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='atalho')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('rg', models.CharField(max_length=11, unique=True, verbose_name='RG')),
                ('date_of_birth', models.DateField(verbose_name='Data de Nascimento')),
                ('sex', models.CharField(choices=[('M', 'MASCULINO'), ('F', 'FEMININO')], max_length=1, verbose_name='Sexo')),
            ],
        ),
    ]
