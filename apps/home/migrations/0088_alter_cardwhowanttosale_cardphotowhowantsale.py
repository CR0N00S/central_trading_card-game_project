# Generated by Django 4.1.4 on 2023-03-13 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0087_alter_cardwhowanttosale_cardphotowhowantsale"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cardwhowanttosale",
            name="cardPhotoWhoWantSale",
            field=models.ImageField(null=True, upload_to="sale_photo"),
        ),
    ]
