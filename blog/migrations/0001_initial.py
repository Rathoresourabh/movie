# Generated by Django 2.1.5 on 2019-02-10 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Publication_Date', models.DateField()),
                ('Body', models.TextField(max_length=500)),
                ('Image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
