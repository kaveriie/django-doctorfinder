# Generated by Django 3.0.4 on 2020-03-27 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20200327_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='usertype',
            new_name='role',
        ),
    ]
