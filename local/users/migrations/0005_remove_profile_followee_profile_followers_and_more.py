# Generated by Django 4.2.3 on 2023-07-13 07:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0004_rename_follow_profile_followee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='followee',
        ),
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(blank=True, null=True, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='followings',
            field=models.ManyToManyField(blank=True, null=True, related_name='followings', to=settings.AUTH_USER_MODEL),
        ),
    ]
