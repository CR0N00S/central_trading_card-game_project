# Generated by Django 4.1.4 on 2023-02-28 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0029_rename_from_nation_card_infomation_card_from_nation"),
    ]

    operations = [
        migrations.AddField(
            model_name="nation_name",
            name="nation_favicon",
            field=models.CharField(max_length=500, null=True),
        ),
    ]
