# Generated by Django 4.2.16 on 2024-09-17 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MessMenu",
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
                ("day", models.CharField(max_length=20)),
                ("breakfast", models.CharField(max_length=200)),
                ("lunch", models.CharField(max_length=200)),
                ("dinner", models.CharField(max_length=200)),
            ],
        ),
    ]
