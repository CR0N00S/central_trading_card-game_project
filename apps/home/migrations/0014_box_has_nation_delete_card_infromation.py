# Generated by Django 4.1.4 on 2023-02-24 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0013_box_infromation_card_infromation"),
    ]

    operations = [
        migrations.CreateModel(
            name="box_has_nation",
            fields=[
                ("b_h_n_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "has_nation",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="home.nation",
                    ),
                ),
                (
                    "id_box",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="home.box_info",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="card_infromation",
        ),
    ]
