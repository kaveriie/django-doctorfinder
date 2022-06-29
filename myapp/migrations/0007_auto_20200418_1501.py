# Generated by Django 3.0.4 on 2020-04-18 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20200415_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songname', models.CharField(max_length=20)),
                ('song', models.FileField(upload_to='myapp/audio/')),
            ],
        ),
        migrations.CreateModel(
            name='VideoGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(null=True, upload_to='myapp/videos/', verbose_name='')),
            ],
        ),
        migrations.RenameModel(
            old_name='Gallery',
            new_name='ImageGallery',
        ),
    ]
