# Generated by Django 2.1.5 on 2019-02-10 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='jobs',
            new_name='job',
        ),
    ]