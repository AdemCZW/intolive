# Generated by Django 4.2.9 on 2024-02-04 14:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0010_uptostock'),
    ]

    operations = [
        migrations.CreateModel(
            name='InToStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=100)),
                ('shipped', models.BooleanField(default=False)),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large'), ('XXL', 'Extra Extra Large'), ('XXXL', 'Triple Extra Large')], default='M', max_length=4)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('color', models.CharField(choices=[('BLK', 'Black'), ('CRM', 'Cream'), ('OAT', 'Oat'), ('CML', 'Camel'), ('BRN', 'Brown')], default='BLK', max_length=3)),
            ],
        ),
    ]
