# Generated by Django 4.2.7 on 2023-11-17 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactme',
            old_name='adress',
            new_name='address',
        ),
    ]
