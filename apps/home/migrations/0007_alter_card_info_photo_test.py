# Generated by Django 3.2.16 on 2023-02-18 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_card_info_photo_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card_info',
            name='photo_test',
            field=models.ImageField(default='ricado.jpg', upload_to='home/upload_img'),
        ),
    ]