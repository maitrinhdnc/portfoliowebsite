# Generated by Django 3.2.5 on 2021-08-08 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_project_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='url',
            new_name='link',
        ),
    ]
