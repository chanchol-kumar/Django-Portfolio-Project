# Generated by Django 4.2.3 on 2024-03-04 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_projectsmodel_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectsmodel',
            name='category',
            field=models.CharField(choices=[('Web Development', 'Web Development'), ('Adroid Development', 'Adroid Development'), ('Django Project ', 'Django Project'), ('Machine Learning', 'Machine Learning')], default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectsmodel',
            name='descriptions',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='projectsmodel',
            name='git_link',
            field=models.URLField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectsmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='projects/media/'),
        ),
        migrations.AlterField(
            model_name='projectsmodel',
            name='live_link',
            field=models.URLField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectsmodel',
            name='technology',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]