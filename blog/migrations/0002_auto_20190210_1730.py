# Generated by Django 2.1.5 on 2019-02-10 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='Publication_Date',
            field=models.DateTimeField(),
        ),
    ]