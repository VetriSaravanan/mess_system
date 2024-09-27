# Generated by Django 4.2.16 on 2024-09-17 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Grocery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("stock_quantity", models.IntegerField()),
                ("unit_price", models.DecimalField(decimal_places=2, max_digits=6)),
                (
                    "daily_consumption",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
                ),
            ],
        ),
    ]
