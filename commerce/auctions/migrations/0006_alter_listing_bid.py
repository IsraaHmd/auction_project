# Generated by Django 5.0.1 on 2024-01-31 18:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0005_listing_bid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="bid",
            field=models.FloatField(default=models.FloatField()),
        ),
    ]
