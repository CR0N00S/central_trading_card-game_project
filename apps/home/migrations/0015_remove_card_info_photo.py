# Generated by Django 3.2.16 on 2023-02-18 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_card_info_photo_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card_info',
            name='photo',
        ),
    ]
