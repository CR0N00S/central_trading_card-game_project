# Generated by Django 3.2.16 on 2023-02-27 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_card_infomation_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='card_infomation',
            name='from_nation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.nation_name'),
        ),
    ]
