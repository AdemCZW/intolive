# Generated by Django 4.2.9 on 2024-03-20 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0012_pickup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='color',
            field=models.CharField(choices=[('BLK', 'Black'), ('CRM', 'Cream'), ('OAT', 'Oat'), ('CML', 'Camel'), ('BRN', 'Brown'), ('WHT', 'White'), ('ORG', 'Orange'), ('GRY', 'Gray'), ('BLU', 'Blue'), ('CAF', 'Caffe'), ('PUR', 'Purple'), ('PNK', 'Pink'), ('BGE', 'Beige'), ('OCL', 'One Color'), ('YLW', 'Yellow')], default='BLK', max_length=10),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='size',
            field=models.CharField(choices=[('XXXS', 'Extra Extra Extra Small'), ('XXS', 'Extra Extra Small'), ('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large'), ('XXL', 'Extra Extra Large'), ('XXXL', 'Triple Extra Large'), ('XXXXL', 'Four Times Extra Large'), ('XXXXXL', 'Five Times Extra Large'), ('XXXXXXL', 'Six Times Extra Large')], default='M', max_length=10),
        ),
    ]
