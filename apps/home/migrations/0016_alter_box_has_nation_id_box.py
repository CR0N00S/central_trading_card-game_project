# Generated by Django 4.1.4 on 2023-02-24 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0015_rename_box_name_test_box_infromation_box_name_n"),
    ]

    operations = [
        migrations.AlterField(
            model_name="box_has_nation",
            name="id_box",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="home.box_infromation",
            ),
        ),
    ]
