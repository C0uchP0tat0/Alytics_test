# Generated by Django 2.2.10 on 2021-08-20 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210819_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='functionmodel',
            name='image',
        ),
    ]
