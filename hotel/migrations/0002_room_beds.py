# Generated by Django 4.2.4 on 2024-03-01 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='beds',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
