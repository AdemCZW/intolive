# Generated by Django 4.2.9 on 2024-01-28 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0003_ingredient_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='color',
            field=models.CharField(choices=[('BLK', 'Black'), ('CRM', 'Cream'), ('OAT', 'Oat'), ('CML', 'Camel'), ('BRN', 'Brown')], default='BLK', max_length=3),
        ),
    ]
