# Generated by Django 4.2.4 on 2023-08-07 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0002_alter_clientes_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedidos',
            old_name='nombre',
            new_name='numero',
        ),
    ]