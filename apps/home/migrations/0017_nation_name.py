# Generated by Django 4.1.4 on 2023-02-24 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0016_alter_box_has_nation_id_box"),
    ]

    operations = [
        migrations.CreateModel(
            name="nation_name",
            fields=[
                (
                    "nation_nam",
                    models.CharField(max_length=500, primary_key=True, serialize=False),
                ),
            ],
        ),
    ]