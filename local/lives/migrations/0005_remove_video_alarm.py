# Generated by Django 4.2.3 on 2023-07-13 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lives', '0004_video_alarm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='alarm',
        ),
    ]
