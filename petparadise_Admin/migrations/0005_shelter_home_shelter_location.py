# Generated by Django 3.2.10 on 2022-03-05 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petparadise_Admin', '0004_order_item_total_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='shelter_home',
            name='shelter_location',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
