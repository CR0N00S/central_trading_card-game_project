# Generated by Django 3.2.16 on 2023-02-27 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_alter_card_infomation_effect_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='card_infomation',
            name='fifth_effect_card',
            field=models.CharField(max_length=500, null=True),
        ),
    ]