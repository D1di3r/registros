# Generated by Django 4.1 on 2022-09-14 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GamePosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre de la Posición')),
                ('description', models.CharField(max_length=50, verbose_name='Descripcion de la Posición')),
            ],
            options={
                'verbose_name': 'Posicion de Juego',
                'verbose_name_plural': 'Posiciones de Juego',
                'db_table': 'posicion',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre del Equipo')),
                ('flagteam', models.ImageField(upload_to='media')),
                ('shieldteam', models.ImageField(upload_to='media')),
            ],
            options={
                'verbose_name': 'Equipo',
                'verbose_name_plural': 'Equipos',
                'db_table': 'equipo',
                'ordering': ['id'],
            },
        ),
    ]