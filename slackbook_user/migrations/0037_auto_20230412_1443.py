# Generated by Django 3.2.18 on 2023-04-12 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slackbook_user', '0036_alter_user_loggedin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='online',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='loggedin',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]