# Generated by Django 4.1.4 on 2023-03-03 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0054_alter_cardwhowanttosale_userwhowantsale"),
    ]

    operations = [
        migrations.AddField(
            model_name="cardwhowanttosale",
            name="userNameWhoWantSale",
            field=models.CharField(
                blank=True, editable=False, max_length=100, null=True
            ),
        ),
    ]
