# Generated by Django 4.2.9 on 2024-01-31 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0004_ingredient_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='category',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
