# Generated by Django 3.2.16 on 2023-02-18 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_card_info_photo_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card_info',
            name='photo_test',
            field=models.ImageField(blank=True, default='ricado_mk2.jpg', null=True, upload_to='apps/static/assets/img_upload'),
        ),
    ]
