# Generated by Django 3.2.18 on 2023-03-29 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slackbook_user', '0006_channel_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='keywords',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='channel',
            name='permission',
            field=models.TextField(blank=True),
        ),
    ]