# Generated by Django 4.1.4 on 2023-03-03 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0049_remove_cardwhowanttosale_cardphotowhowantsale_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cardwhowanttosale",
            old_name="cardSaleCode",
            new_name="card_code",
        ),
    ]
