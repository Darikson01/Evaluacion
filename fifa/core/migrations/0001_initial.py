# Generated by Django 4.1.1 on 2022-09-16 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Nombre del equipo')),
                ('flag', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen de la bandera')),
                ('shield', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Escudo del equipo')),
            ],
            options={
                'verbose_name': 'Equipo',
                'verbose_name_plural': 'Equipos',
                'db_table': 'equipo',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre de la posición')),
                ('description', models.TextField(null=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Posicion',
                'verbose_name_plural': 'Posiciones',
                'db_table': 'posicion',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Technical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre de la posición')),
                ('surname', models.CharField(max_length=30, verbose_name='Apellido del jugador')),
                ('birth', models.DateField(verbose_name='Fecha de nacimiendo')),
                ('Nationality', models.TextField(verbose_name='Nombre de la posición')),
            ],
            options={
                'verbose_name': 'Tecnico',
                'verbose_name_plural': 'Tecnicos',
                'db_table': 'tecnico',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre del jugador')),
                ('surname', models.CharField(max_length=30, verbose_name='Apellido del jugador')),
                ('photo', models.ImageField(null=True, upload_to='Imagenes_jugadores/', verbose_name='Foto del jugador')),
                ('birth', models.DateField(verbose_name='Fecha de nacimiendo')),
                ('tshirt', models.IntegerField(verbose_name='Numero de camiseta')),
                ('headline', models.BooleanField(verbose_name='¿El jugador es titular?')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.equipment')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.position')),
            ],
            options={
                'verbose_name': 'Jugador',
                'verbose_name_plural': 'Jugadores',
                'db_table': 'jugador',
                'ordering': ['id'],
            },
        ),
    ]
