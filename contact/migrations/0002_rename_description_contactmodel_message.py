# Generated by Django 4.2.3 on 2024-02-04 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmodel',
            old_name='Description',
            new_name='Message',
        ),
    ]
