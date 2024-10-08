# Generated by Django 4.2.4 on 2023-11-29 22:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proinso_app', '0004_alter_cliente_fecha_nacimiento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(1993, 12, 6, 22, 3, 52, 58154, tzinfo=datetime.timezone.utc), verbose_name='Fecha Nacimiento'),
        ),
        migrations.AlterField(
            model_name='tipodocumento',
            name='tipo',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 6, 22, 3, 52, 65775, tzinfo=datetime.timezone.utc), verbose_name='Fecha Instalacion'),
        ),
    ]
