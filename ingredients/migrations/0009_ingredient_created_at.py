# Generated by Django 4.2.9 on 2024-01-31 15:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0008_ingredient_shipped'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
