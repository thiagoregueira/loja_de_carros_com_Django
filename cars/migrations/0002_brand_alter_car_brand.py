# Generated by Django 5.0 on 2023-12-18 15:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cars", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name="car",
            name="brand",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="car_brand",
                to="cars.brand",
            ),
        ),
    ]
