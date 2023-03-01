# Generated by Django 3.2.16 on 2023-02-27 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_box_infromation_box_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='card_infomation',
            fields=[
                ('card_code', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('card_name_new', models.CharField(max_length=500)),
                ('effect_card', models.CharField(max_length=500)),
                ('price_average', models.IntegerField()),
                ('card_photo', models.ImageField(blank=True, default='no_infomation.png', null=True, upload_to='card_img')),
            ],
        ),
    ]