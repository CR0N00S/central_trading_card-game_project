# Generated by Django 4.1.4 on 2023-03-06 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0068_alter_transaction_table_buyerphone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction_table",
            name="card_code",
            field=models.CharField(editable=False, max_length=500, null=True),
        ),
    ]