# Generated by Django 4.1.4 on 2023-03-02 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0012_auto_20230302_0030"),
        ("home", "0044_rename_card_code_cardwhowanttosale_cardsalecode"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cardwhowanttosale",
            name="userWhoWantSale",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="authentication.profile",
            ),
        ),
    ]
