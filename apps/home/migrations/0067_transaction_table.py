# Generated by Django 4.1.4 on 2023-03-06 10:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0066_delete_card_info_delete_nation"),
    ]

    operations = [
        migrations.CreateModel(
            name="transaction_table",
            fields=[
                (
                    "transaction_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "fromSalerUser",
                    models.CharField(editable=False, max_length=100, null=True),
                ),
                (
                    "toBuyerUser",
                    models.CharField(editable=False, max_length=100, null=True),
                ),
                (
                    "buyerAddr",
                    models.CharField(editable=False, max_length=500, null=True),
                ),
                ("buyerPhone", models.CharField(blank=True, max_length=10, null=True)),
                ("saleDay", models.DateTimeField(auto_now_add=True)),
                (
                    "card_code",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="home.card_infomation",
                    ),
                ),
            ],
        ),
    ]
