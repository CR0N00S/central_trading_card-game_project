# Generated by Django 4.1.4 on 2023-03-02 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0043_rename_cardsalecode_cardwhowanttosale_card_code"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cardwhowanttosale",
            old_name="card_code",
            new_name="cardSaleCode",
        ),
    ]
