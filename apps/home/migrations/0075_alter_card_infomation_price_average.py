# Generated by Django 4.1.4 on 2023-03-07 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0074_transaction_table_price_detal"),
    ]

    operations = [
        migrations.AlterField(
            model_name="card_infomation",
            name="price_average",
            field=models.IntegerField(default=0),
        ),
    ]
