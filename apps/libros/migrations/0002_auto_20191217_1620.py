# Generated by Django 3.0 on 2019-12-17 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='genero',
            field=models.CharField(choices=[('NO', 'Novela'), ('CF', 'Ciencia_Ficcion'), ('FA', 'Fantasia'), ('RO', 'Romance'), ('CU', 'Cuentos'), ('PO', 'Poesia'), ('RE', 'Relato')], max_length=2),
        ),
    ]
