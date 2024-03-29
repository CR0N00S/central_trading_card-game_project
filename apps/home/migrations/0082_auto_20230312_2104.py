# Generated by Django 3.2.16 on 2023-03-12 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0081_alter_rating_rating_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rate',
            field=models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=150),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rateUser',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='userWhoRateThis',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
