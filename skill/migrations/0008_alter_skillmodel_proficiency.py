# Generated by Django 4.2.3 on 2024-02-04 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0007_alter_skillmodel_proficiency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillmodel',
            name='proficiency',
            field=models.IntegerField(choices=[(25, 'Beginner'), (50, 'Intermediate'), (75, 'Advanced'), (100, 'Expert')]),
        ),
    ]
