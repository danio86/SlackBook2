# Generated by Django 3.2.18 on 2023-04-11 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slackbook_user', '0032_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_description',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
