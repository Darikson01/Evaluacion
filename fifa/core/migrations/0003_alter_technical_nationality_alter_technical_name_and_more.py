# Generated by Django 4.1.1 on 2022-09-16 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_player_equipment_alter_player_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technical',
            name='Nationality',
            field=models.CharField(max_length=40, verbose_name='Nacionalidad'),
        ),
        migrations.AlterField(
            model_name='technical',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Nombre del tecnico'),
        ),
        migrations.AlterField(
            model_name='technical',
            name='surname',
            field=models.CharField(max_length=30, verbose_name='Apellido del tecnico'),
        ),
    ]