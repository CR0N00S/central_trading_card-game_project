# Generated by Django 4.1.4 on 2023-02-23 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0010_remove_card_info_nation"),
    ]

    operations = [
        migrations.AddField(
            model_name="card_info",
            name="from_nation",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="home.nation",
            ),
        ),
    ]
