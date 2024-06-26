# Generated by Django 4.2.9 on 2024-01-31 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0005_remove_ingredient_category_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large'), ('2XL', 'Extra Extra Large'), ('3XL', 'Triple Extra Large')], default='M', max_length=4),
        ),
    ]
