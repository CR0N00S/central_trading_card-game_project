# Generated by Django 3.2.16 on 2023-02-21 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_photo',
            field=models.ImageField(blank=True, default='icon-van.jpg', null=True, upload_to='user_icon'),
        ),
    ]
