# Generated by Django 4.2.16 on 2024-09-17 02:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("notifications", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="notification",
            old_name="date_sent",
            new_name="timestamp",
        ),
        migrations.RemoveField(
            model_name="notification",
            name="notification_type",
        ),
        migrations.RemoveField(
            model_name="notification",
            name="student",
        ),
        migrations.AddField(
            model_name="notification",
            name="is_read",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="notification",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
