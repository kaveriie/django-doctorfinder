# Generated by Django 3.0.4 on 2020-05-18 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_auto_20200518_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='paymentmethod',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='payment',
            name='paymentstatus',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
