# Generated by Django 4.2.3 on 2024-02-06 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_projectsmodel_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectsmodel',
            name='category',
            field=models.CharField(blank=True, choices=[('HTML & CSS', 'HTML & CSS'), ('java-scripts', 'java-scripts'), ('Django', 'Django'), ('Machine Learning', 'Machine Learning'), ('App Delvelopment', 'App Delvelopment')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='projectsmodel',
            name='technology',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
