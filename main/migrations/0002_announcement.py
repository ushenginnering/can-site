# Generated by Django 4.2.9 on 2024-01-12 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Announcement",
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
                ("image", models.ImageField(upload_to="Announcement")),
                ("headline", models.CharField(max_length=100)),
                ("body", models.TextField()),
            ],
        ),
    ]
