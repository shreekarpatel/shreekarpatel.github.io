# Generated by Django 3.2.10 on 2022-02-12 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petparadise_Admin', '0002_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='rate',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
