# Generated by Django 4.2.1 on 2023-07-09 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codigo', '0009_boleta_detalle_boleta'),
    ]

    operations = [
        migrations.AddField(
            model_name='boleta',
            name='envio',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='boleta',
            name='impuestos',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
