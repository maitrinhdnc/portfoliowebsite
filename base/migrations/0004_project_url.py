# Generated by Django 3.2.5 on 2021-08-08 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_project_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.CharField(default=True, max_length=200),
        ),
    ]
