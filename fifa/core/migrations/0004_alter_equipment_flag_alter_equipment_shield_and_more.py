# Generated by Django 4.1.1 on 2022-09-18 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_technical_nationality_alter_technical_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='flag',
            field=models.ImageField(null=True, upload_to='media/', verbose_name='Escudo del equipo'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='shield',
            field=models.ImageField(null=True, upload_to='media/', verbose_name='Escudo del equipo'),
        ),
        migrations.AlterField(
            model_name='player',
            name='photo',
            field=models.ImageField(null=True, upload_to='media/', verbose_name='Foto del jugador'),
        ),
    ]
