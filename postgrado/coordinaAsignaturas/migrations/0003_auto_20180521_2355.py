# Generated by Django 2.0.4 on 2018-05-21 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordinaAsignaturas', '0002_auto_20180521_2320'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='oferta',
            options={'ordering': ('anio',)},
        ),
        migrations.RemoveField(
            model_name='asignatura',
            name='nomProf',
        ),
        migrations.RemoveField(
            model_name='asignatura',
            name='ofertas',
        ),
        migrations.AddField(
            model_name='oferta',
            name='asignaturas',
            field=models.ManyToManyField(to='coordinaAsignaturas.Asignatura'),
        ),
    ]
