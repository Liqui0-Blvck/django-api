# Generated by Django 5.0.1 on 2024-01-14 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario_snab', '0003_proveedor_direccion_alter_proveedor_contacto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordendecompra',
            name='productos',
        ),
    ]
