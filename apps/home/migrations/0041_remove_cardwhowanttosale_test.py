# Generated by Django 4.1.4 on 2023-03-02 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0040_cardwhowanttosale_test"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cardwhowanttosale",
            name="test",
        ),
    ]