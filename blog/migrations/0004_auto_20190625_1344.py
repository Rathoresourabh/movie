# Generated by Django 2.1.5 on 2019-06-25 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190216_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='Title',
            new_name='title',
        ),
    ]
