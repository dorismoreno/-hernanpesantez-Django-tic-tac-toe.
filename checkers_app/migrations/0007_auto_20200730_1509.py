# Generated by Django 3.0.8 on 2020-07-30 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkers_app', '0006_usermoves_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermoves',
            name='moves',
            field=models.CharField(max_length=120),
        ),
    ]
