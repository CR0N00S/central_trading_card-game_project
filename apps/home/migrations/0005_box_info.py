# Generated by Django 4.1.4 on 2023-02-22 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_card_info"),
    ]

    operations = [
        migrations.CreateModel(
            name="box_info",
            fields=[
                ("box_id", models.AutoField(primary_key=True, serialize=False)),
                ("box_name", models.CharField(max_length=500)),
                ("number_of_card", models.IntegerField()),
                ("num_rarity_c", models.IntegerField()),
                ("num_rarity_r", models.IntegerField()),
                ("num_rarity_rr", models.IntegerField()),
                ("num_rarity_rrr", models.IntegerField()),
                ("day_add", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
