# Generated by Django 5.0 on 2023-12-18 15:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cars", "0002_brand_alter_car_brand"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="plate",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]