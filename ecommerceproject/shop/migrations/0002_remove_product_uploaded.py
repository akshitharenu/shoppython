# Generated by Django 3.2.8 on 2021-12-13 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='uploaded',
        ),
    ]
