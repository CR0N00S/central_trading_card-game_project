# Generated by Django 4.1.4 on 2023-03-03 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0063_alter_cardwhowanttosale_cardphotowhowantsale"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cardwhowanttosale",
            name="cardPhotoWhoWantSale",
            field=models.ImageField(default="", null=True, upload_to="sale_photo/"),
        ),
    ]
