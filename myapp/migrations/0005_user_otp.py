# Generated by Django 3.0.4 on 2020-04-14 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20200327_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.IntegerField(default='1234'),
        ),
    ]