# Generated by Django 4.0.5 on 2022-07-15 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitioPet', '0008_alter_customer_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoCompra',
            fields=[
                ('idEstado', models.PositiveSmallIntegerField(primary_key=True, serialize=False, verbose_name='Id del estado de compra')),
                ('estado', models.CharField(max_length=25, verbose_name='(En preparación,En despacho,Entregado)')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('idCompra', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Id de la compra')),
                ('cod_bol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitioPet.boleta')),
                ('cod_estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitioPet.estadocompra')),
            ],
        ),
    ]
