<<<<<<< HEAD
# Generated by Django 4.1.4 on 2023-03-02 09:21
=======
# Generated by Django 3.2.16 on 2023-03-02 11:37
>>>>>>> ce5ae8672963869abb7e8b056bd1a2562ffb6ada

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
<<<<<<< HEAD
        ("home", "0032_alter_nation_name_nation_favicon"),
=======
        ('home', '0032_alter_nation_name_nation_favicon'),
>>>>>>> ce5ae8672963869abb7e8b056bd1a2562ffb6ada
    ]

    operations = [
        migrations.AlterField(
<<<<<<< HEAD
            model_name="card_infomation",
            name="effect_card",
=======
            model_name='card_infomation',
            name='effect_card',
>>>>>>> ce5ae8672963869abb7e8b056bd1a2562ffb6ada
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
    ]
