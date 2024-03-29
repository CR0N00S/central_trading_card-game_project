# Generated by Django 4.1.4 on 2023-03-01 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("authentication", "0010_remove_profile_user_profile_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="password",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="surname",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="username",
        ),
        migrations.AddField(
            model_name="profile",
            name="user",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
