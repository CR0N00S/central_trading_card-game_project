# Generated by Django 4.1.4 on 2023-03-03 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0060_alter_cardwhowanttosale_cardphotowhowantsale"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cardwhowanttosale",
            name="cardPhotoWhoWantSale",
            field=models.ImageField(
                default="no_infomation.png", null=True, upload_to="sale_photo"
            ),
        ),
    ]
