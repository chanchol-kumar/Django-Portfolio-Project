# Generated by Django 4.2.3 on 2024-02-06 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsmodel',
            name='category',
            field=models.CharField(choices=[('HTML & CSS', 'HTML & CSS'), ('java-scripts', 'java-scripts'), ('Django', 'Django'), ('Machine Learning', 'Machine Learning'), ('App Delvelopment', 'App Delvelopment')], default='HTML & CSS', max_length=30),
        ),
    ]
