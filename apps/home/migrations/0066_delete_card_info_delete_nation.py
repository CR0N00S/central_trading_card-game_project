# Generated by Django 4.1.4 on 2023-03-06 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0065_alter_cardwhowanttosale_cardphotowhowantsale"),
    ]

    operations = [
        migrations.DeleteModel(
            name="card_info",
        ),
        migrations.DeleteModel(
            name="nation",
        ),
    ]
