# Generated by Django 4.0.6 on 2022-07-24 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='msg',
            field=models.TextField(max_length=500),
        ),
    ]