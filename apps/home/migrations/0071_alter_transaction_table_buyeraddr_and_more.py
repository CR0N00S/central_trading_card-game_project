# Generated by Django 4.1.4 on 2023-03-06 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0070_alter_transaction_table_buyeraddr_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction_table",
            name="buyerAddr",
            field=models.CharField(editable=False, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="transaction_table",
            name="buyerPhone",
            field=models.CharField(editable=False, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="transaction_table",
            name="card_code",
            field=models.CharField(editable=False, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="transaction_table",
            name="fromSalerUser",
            field=models.CharField(editable=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="transaction_table",
            name="toBuyerUser",
            field=models.CharField(editable=False, max_length=100, null=True),
        ),
    ]
