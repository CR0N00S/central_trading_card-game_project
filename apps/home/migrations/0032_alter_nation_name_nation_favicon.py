# Generated by Django 3.2.16 on 2023-03-01 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_alter_card_infomation_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nation_name',
            name='nation_favicon',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
