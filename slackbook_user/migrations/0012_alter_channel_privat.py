# Generated by Django 3.2.18 on 2023-04-01 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slackbook_user', '0011_alter_channel_privat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='privat',
            field=models.BooleanField(default=True),
        ),
    ]
