# Generated by Django 3.0.4 on 2020-05-15 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20200515_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='booking',
            name='dob',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='booking',
            name='phoneno',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='booking',
            name='service',
            field=models.CharField(max_length=30),
        ),
    ]
