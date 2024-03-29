# Generated by Django 4.2.9 on 2024-01-31 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0006_alter_ingredient_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large'), ('XXL', 'Extra Extra Large'), ('XXXL', 'Triple Extra Large')], default='M', max_length=4),
        ),
    ]
