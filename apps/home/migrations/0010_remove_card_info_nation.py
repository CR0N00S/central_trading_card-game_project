# Generated by Django 4.1.4 on 2023-02-23 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0009_box_info_bt_num"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="card_info",
            name="nation",
        ),
    ]
