# Generated by Django 4.2.9 on 2024-02-03 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0009_ingredient_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uptostock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredients.ingredient')),
            ],
        ),
    ]
