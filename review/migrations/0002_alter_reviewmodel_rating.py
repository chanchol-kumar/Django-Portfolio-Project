# Generated by Django 4.2.3 on 2024-02-03 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewmodel',
            name='Rating',
            field=models.CharField(choices=[('★☆☆☆☆☆☆', '★☆☆☆☆☆☆'), ('★★☆☆☆☆☆', '★★☆☆☆☆☆'), ('★★★☆☆☆☆', '★★★☆☆☆☆'), ('★★★★☆☆☆', '★★★★☆☆☆'), ('★★★★★☆☆', '★★★★★☆☆'), ('★★★★★★☆', '★★★★★★☆'), ('★★★★★★★', '★★★★★★★')], max_length=7),
        ),
    ]
