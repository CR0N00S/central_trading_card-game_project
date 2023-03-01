# Generated by Django 4.1.4 on 2023-02-23 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0007_transaction"),
    ]

    operations = [
        migrations.AddField(
            model_name="card_info",
            name="from_box",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="home.box_info",
            ),
        ),
    ]