# Generated by Django 4.1.4 on 2023-03-03 07:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("home", "0046_alter_cardwhowanttosale_cardphotowhowantsale_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cardwhowanttosale",
            name="userWhoWantSale",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
